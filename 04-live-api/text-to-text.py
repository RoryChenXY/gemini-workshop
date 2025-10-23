"""
This script lets you chat live with Gemini

Ensure the `GEMINI_API_KEY` environment variable is set to the api-key
you obtained from Google AI Studio.
"""
import asyncio
import os

from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

model = "gemini-live-2.5-flash-preview"

config = {"response_modalities": ["TEXT"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session Started. Type 'exit' to end the session")

        while (message := input("> ")) != "exit":

            await session.send_client_content(
                turns={
                    "role": "user",
                    "parts": [{"text": message}]},
                turn_complete=True
            )

            async for response in session.receive():
                if response.text is not None:
                    print(response.text, end="")


if __name__ == "__main__":
    asyncio.run(main())
