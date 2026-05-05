import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Download YouTube videos from the command line"
    )
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "-o", "--output",
        default="downloads",
        help="Output directory (default: downloads)"
    )
    parser.add_argument(
        "-q", "--quality",
        default="best",
        help="Video quality: best, 720p, 480p, audio-only"
    )

    args = parser.parse_args()
    print(f"URL: {args.url}")
    print(f"Output: {args.output}")
    print(f"Quality: {args.quality}")
    print("Setup complete! Ready to build.")

if __name__ == "__main__":
    main()