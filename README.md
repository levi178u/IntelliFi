# IntelliFi - Intelligent Financial Analysis Platform

IntelliFi is a comprehensive financial analysis platform that combines real-time cryptocurrency price data, news analysis, and intelligent alerts to provide users with actionable insights for their investment decisions.

## Features

- **Real-time Price Tracking**: Monitor cryptocurrency prices with real-time updates
- **News Analysis**: Get relevant financial news and market insights
- **Smart Alerts**: Receive intelligent alerts based on price movements and market conditions
- **AI Assistant**: Interact with an AI agent for market analysis and insights
- **Blockchain Integration**: Seamless integration with Exsat blockchain network

## Prerequisites

- Docker and Docker Compose
- News API Key (from [NewsAPI](https://newsapi.org/))
- Git

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/your-username/intellifi.git
cd intellifi
```

2. Set up environment variables:
```bash
export NEWS_API_KEY=your_news_api_key_here
```

3. Start the services:
```bash
./start.sh
```

## Architecture

The platform consists of several microservices:

### Backend Services

- **Price Service** (Port 8000)
  - Real-time cryptocurrency price tracking
  - Historical price data
  - Price analysis and trends

- **News Service** (Port 8001)
  - Financial news aggregation
  - News sentiment analysis
  - Market impact assessment

- **Alerts Service** (Port 8002)
  - Custom alert creation
  - Price movement notifications
  - Market condition alerts

- **Agent Service** (Port 8003)
  - AI-powered market analysis
  - Natural language interaction
  - Investment recommendations

### Frontend

- **Web Interface** (Port 80)
  - Modern, responsive design
  - Real-time data visualization
  - Interactive dashboards

### Blockchain Integration

- **Exsat Node** (Port 8545)
  - Blockchain data access
  - Smart contract interaction
  - Transaction monitoring

## Service URLs

- Frontend: http://localhost
- Price API: http://localhost:8000
- News API: http://localhost:8001
- Alerts API: http://localhost:8002
- Agent API: http://localhost:8003
- Exsat Node: http://localhost:8545

## Configuration

### Environment Variables

- `NEWS_API_KEY`: Your NewsAPI key
- `EXSAT_NODE_URL`: Exsat node connection URL (default: http://exsat-node:8545)

### Docker Configuration

The project uses Docker Compose for orchestration. Key configurations:

- All services are connected through the `intellifi-network`
- Persistent storage for Exsat node data
- Health checks for all services
- Automatic service restart on failure

## Development

### Project Structure

```
intellifi/
├── Agents/              # Backend services
│   ├── Dockerfile.price
│   ├── Dockerfile.news
│   ├── Dockerfile.alerts
│   └── Dockerfile.agent
├── Client/             # Frontend application
│   └── Dockerfile
├── docker-compose.yml  # Service orchestration
├── nginx.conf         # Web server configuration
├── start.sh          # Startup script
└── README.md         # This file
```

### Building Services

To build individual services:

```bash
docker-compose build [service_name]
```

Available services:
- price
- news
- alerts
- agent
- frontend
- exsat-node

### Health Checks

All services include health check endpoints at `/health`. The startup script verifies service health before proceeding.

## Troubleshooting

### Common Issues

1. **Service Not Starting**
   - Check Docker logs: `docker-compose logs [service_name]`
   - Verify environment variables
   - Check service dependencies

2. **Connection Issues**
   - Verify network connectivity
   - Check service health endpoints
   - Ensure Exsat node is running

3. **Data Persistence**
   - Check volume mounting
   - Verify permissions
   - Check disk space

### Logs

View service logs:
```bash
docker-compose logs -f [service_name]
```

## Contributing

1. Fork the repository
<<<<<<< Updated upstream
2. Create your feature branch (`git checkout -b feature/home`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/home`)
5. Open a Pull Request

## API Documentation
https://documenter.getpostman.com/view/41487613/2sB2qZEMr5
=======
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Your License Here]

## Support

For support, please [open an issue](https://github.com/your-username/intellifi/issues) or contact the development team.
>>>>>>> Stashed changes
