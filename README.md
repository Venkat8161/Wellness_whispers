# Wellness Whispers

A Python-based application that sends wellness messages and reminders through WhatsApp using the GupShup API and OpenAI integration.

## Features

- Generates personalized wellness messages using OpenAI
- Sends messages through WhatsApp using GupShup API
- Easy to configure and customize

## Project Structure

```
├── app.py                 # Main application file
├── assets/               
│   └── logo.png          # Project logo
└── utils/
    ├── message_generator.py  # Message generation logic
    └── whatsapp_sender.py   # WhatsApp sending functionality
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Venkat8161/Wellness_whispers.git
cd Wellness_whispers
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key
   - Add your GupShup API credentials

## Environment Variables

The following environment variables are required:

- `OPENAI_API_KEY`: Your OpenAI API key
- `GUPSHUP_API_KEY`: Your GupShup API key
- `GUPSHUP_SENDER_ID`: Your registered sender number/ID for GupShup

## Usage

Run the application:
```bash
python app.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the API for message generation
- GupShup for WhatsApp integration capabilities
