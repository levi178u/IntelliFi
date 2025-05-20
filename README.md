# IntelliFi - Crypto Intelligence Platform

A modern cryptocurrency intelligence platform with real-time price tracking, news aggregation, price alerts, and an AI assistant.

## Features

- Real-time cryptocurrency price tracking
- Latest crypto news feed
- Price alerts and notifications
- AI-powered assistant for crypto queries
- Dark/Light mode
- Responsive design
- Integration with exSat network

## Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.9+ (for local development)
- News API key (for news service)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/intellifi.git
cd intellifi
```

2. Create a `.env` file in the root directory:
```bash
NEWS_API_KEY=your_news_api_key_here
```

3. Build and start the services:
```bash
docker-compose up --build
```

The application will be available at `http://localhost`.

## Development

### Frontend (Svelte)

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

### Backend Services

Each service can be run independently:

```bash
# Price service
python price.py

# News service
python news.py

# Alerts service
python alerts.py

# Agent service
python agent.py
```

## Architecture

- Frontend: Svelte + TailwindCSS
- Backend: FastAPI (Python)
- Database: exSat network integration
- Containerization: Docker

## API Endpoints

- Price Service: `http://localhost:8000`
- News Service: `http://localhost:8001`
- Alerts Service: `http://localhost:8002`
- Agent Service: `http://localhost:8003`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.