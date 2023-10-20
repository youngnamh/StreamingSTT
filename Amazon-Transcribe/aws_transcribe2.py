
from print_speakers import execute
from amazon_transcribe.model import TranscriptEvent
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.client import TranscribeStreamingClient
import asyncio
# This example uses the sounddevice library to get an audio stream from the
# microphone. It's not a dependency of the project but can be installed with
# `python -m pip install amazon-transcribe aiofile`
# `pip install sounddevice`.
import aiofile
import sounddevice
import nest_asyncio
import time
import json

nest_asyncio.apply()


"""
Here's an example of a custom event handler you can extend to
process the returned transcription results as needed. This
handler will simply print the text out to your interpreter.
"""


class MyEventHandler(TranscriptResultStreamHandler):
    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        # This handler can be implemented to handle transcriptions as needed.
        # Here's an example to get started.

        results = transcript_event.transcript.results

        # go through each alt and print the transcript
        for result in results:
            is_partial = result.is_partial
            for alt in result.alternatives:
                print(alt.transcript)
                if is_partial == False:
                    items = alt.items
                    wordData = []
                    for item in items:
                        content = item.content
                        confidence = item.confidence
                        speaker = item.speaker
                        wordData.append([speaker, content, confidence])
                        # print(f"(speaker{speaker}: {content},{confidence})")
                    execute(wordData)

                # transcript_event_json = json.dumps(transcript_event, default=lambda o: o.__dict__, indent=4)
                # print(f"[json] {transcript_event_json}")


async def mic_stream():
    # This function wraps the raw input stream from the microphone forwarding
    # the blocks to an asyncio.Queue.
    loop = asyncio.get_event_loop()
    input_queue = asyncio.Queue()

    def callback(indata, frame_count, time_info, status):
        loop.call_soon_threadsafe(
            input_queue.put_nowait, (bytes(indata), status))

    # Be sure to use the correct parameters for the audio stream that matches
    # the audio formats described for the source language you'll be using:
    # https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html
    stream = sounddevice.RawInputStream(
        channels=1,
        samplerate=16000,
        callback=callback,
        blocksize=1024 * 2,
        dtype="int16",
    )
    # Initiate the audio stream and asynchronously yield the audio chunks
    # as they become available.
    with stream:
        while True:
            indata, status = await input_queue.get()
            yield indata, status


async def write_chunks(stream):
    # This connects the raw audio chunks generator coming from the microphone
    # and passes them along to the transcription stream.
    async for chunk, status in mic_stream():
        await stream.input_stream.send_audio_event(audio_chunk=chunk)
    await stream.input_stream.end_stream()


async def basic_transcribe():
    # Setup up our client with our chosen AWS region
    client = TranscribeStreamingClient(region="us-east-1")

    # Start transcription to generate our async stream
    stream = await client.start_stream_transcription(
        language_code="en-US",
        media_sample_rate_hz=16000,
        media_encoding="pcm",
        show_speaker_label=True
    )
    # Instantiate our handler and start processing events
    # global start_time
    # start_time = time.time()
    handler = MyEventHandler(stream.output_stream)
    await asyncio.gather(write_chunks(stream), handler.handle_events())

'''
def print_latency(start, end):
    global counter
    global latency_arr
    latency = end - start  # Calculate the elapsed time (latency)
    if(counter != 0):
        latency_arr.append(latency)
    counter += 1
    if (counter % 50 == 0):
        latency_ave = sum(latency_arr) / len(latency_arr)
        print(f"Latency : {latency_ave} seconds")
'''


loop = asyncio.get_event_loop()
loop.run_until_complete(basic_transcribe())

loop.close()
