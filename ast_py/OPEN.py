from pocketsphinx import LiveSpeech

# Simple wake word listener
def listen_for_wake_word(wake_word="computer"):
    speech = LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        keyphrase=wake_word,
        kws_threshold=1e-20 # Adjust this for sensitivity
    )
    for phrase in speech:
        print(f"Wake word '{wake_word}' detected!")
        return True

# Main loop with wake word
while True:
    print("Waiting for wake word...")
    listen_for_wake_word()
    run_assistant() # Run the main assistant after wake word is heard