#
# Copyright (c) 2020 Manolis Stamatogiannakis.
#
# This file is part of Google Cloud Subs.
# The project is not affiliated with Google LLC in any way.
# See https://github.com/m000/google-cloud-subs for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import argparse
import json
import logging
import re
import sys
import srt
import datetime

def make_subs_fixed(response, bin_size=3000):
    """ Create subtitles that fit in fixed size bins.
        This is the method used by the original Medium article.

        The produced output should be identical, minus a few rounding errors.
        The rounding errors are introduced when the protobuf result is exported
        as json for this script to process. It involves rounding 0.099sec to 
        0.100sec. This is arguably an improvement.
    """
    transcriptions = []
    index = 0
    results = response['results']

    for result in results:
        words = result['alternatives'][0].get('words', None)
        if words is None:
            continue

        # start/end times for result (sorted?)
        bin_start = words[0].get('startTime', 0)
        bin_end = bin_start + bin_size

        # last word end
        last_end = words[-1].get('endTime', 0)

        # bin transcript
        transcript = words[0]['word']

        # subtitle index
        index += 1

        for i, w in enumerate(words[1:], 1):
            word = w['word']
            word_start = w.get('startTime', 0)
            word_end = w.get('endTime', 0)

            if word_end//1000 < bin_end//1000:
                transcript = transcript + " " + word
            else:
                # append bin transcript
                sub_start = datetime.timedelta(milliseconds=bin_start)
                sub_end = datetime.timedelta(milliseconds=words[i-1].get('endTime', 0))
                transcriptions.append(srt.Subtitle(index, sub_start, sub_end, transcript))

                # increment index and reset bin
                index += 1
                bin_start = word_start
                bin_end = bin_start + bin_size
                transcript = word

        # append transcript of last transcript in bin
        sub_start = datetime.timedelta(milliseconds=bin_start)
        sub_end = datetime.timedelta(milliseconds=last_end)
        transcriptions.append(srt.Subtitle(index, sub_start, sub_end, transcript))
        index += 1

    # turn transcription list into subtitles
    subtitles = srt.compose(transcriptions)
    return subtitles


def main():
    # parse arguments
    parser = argparse.ArgumentParser(
        description="Convert a Google Transcription log file to srt.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-o", "--output", default=None,
        help="output file")
    parser.add_argument("input", nargs="?", help="input file")
    args = parser.parse_args()

    # read transcript json file and convert times to usec
    time_re = re.compile(r'^([\d.]+)(s)$')
    def timeconv(jsonobj):
        for k in ['startTime', 'endTime']:
            if k not in jsonobj: continue
            m = time_re.match(jsonobj[k])
            assert m is not None, "Bad time specification: %r" % jsonobj[k]
            jsonobj[k] = int(float(m[1]) * 1000)
        return jsonobj
    if args.input is None:
        transcript = json.load(sys.stdin, object_hook=timeconv)
    else:
        with open(args.input, "r") as f:
            transcript = json.load(f, object_hook=timeconv)

    print(make_subs_fixed(transcript))

if __name__ == '__main__':
    main()

