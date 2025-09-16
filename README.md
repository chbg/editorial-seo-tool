# Editorial SEO Content Generation Tool

A powerful AI-driven content generation tool designed for editorial teams and content marketers. This tool helps create high-quality, SEO-optimized articles with precise keyword targeting and natural language integration.

## Features

- **AI-Powered Content Generation**: Uses OpenAI's GPT models for intelligent content creation
- **Advanced Keyword Management**: Primary keyword (3-5x) and supporting keywords (1-2x each) integration
- **Multiple Article Types**: General articles and list-based articles with company recommendations
- **Client Management**: Store and manage client-specific tone, voice, and AI artifact preferences
- **Article Management**: Save, load, search, and organize generated articles
- **Real-time Progress Tracking**: Visual progress indicators and verbose loading states
- **Content Review System**: Grammar, style, and AI artifact detection and correction

## Deployment

This application is deployed on Netlify and automatically updates when changes are pushed to the main branch.

### Environment Variables

The following environment variables need to be set in Netlify:

- `OPENAI_API_KEY`: Your OpenAI API key for content generation

### Local Development

To run locally:

```bash
# Using Python (recommended)
python -m http.server 8000

# Or using Node.js
npm start
```

Then open `http://localhost:8000` in your browser.

## Usage

1. **Set up your OpenAI API key** in the settings
2. **Select a client** from the dropdown or create a new one
3. **Enter your article details**:
   - Topic
   - Primary keyword (targeted 3-5 times)
   - Supporting keywords (1-2 times each, max 9)
   - Article type (General or List-based)
4. **Generate your article** and review the results
5. **Save and manage** your articles for future reference

## Technical Details

- **Frontend**: Pure HTML, CSS, and JavaScript (no frameworks)
- **AI Integration**: OpenAI GPT models via API
- **Storage**: Local storage for client data and article drafts
- **Deployment**: Netlify with automatic GitHub integration
- **Security**: HTTPS with security headers and CORS protection

## Support

For issues or questions, please contact the development team or create an issue in the repository.

## License

MIT License - see LICENSE file for details.
