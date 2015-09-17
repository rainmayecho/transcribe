from stream import AudioStream

def main():
    stream = AudioStream()
    stream.setup()
    stream.start_record()        

if __name__ == '__main__':
    main()
