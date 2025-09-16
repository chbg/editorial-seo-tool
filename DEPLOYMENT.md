# Netlify Deployment Instructions

## Prerequisites

1. **GitHub Account**: You'll need a GitHub account to host the repository
2. **Netlify Account**: Sign up at [netlify.com](https://netlify.com)
3. **OpenAI API Key**: Get your API key from [OpenAI](https://platform.openai.com/api-keys)

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it `editorial-seo-tool` (or your preferred name)
3. Make it public or private (your choice)
4. **Don't** initialize with README, .gitignore, or license (we already have these)

## Step 2: Initialize Git and Push to GitHub

```bash
# Navigate to the deployment folder
cd /Users/houstonbarnett-gearhart/Desktop/vibes-only/dupea-netlify

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Editorial SEO Tool deployment ready"

# Add your GitHub repository as origin (replace with your actual repo URL)
git remote add origin https://github.com/chbg/editorial-seo-tool.git

# Push to GitHub
git push -u origin main
```

## Step 3: Deploy to Netlify

1. Go to [Netlify](https://app.netlify.com)
2. Click "New site from Git"
3. Choose "GitHub" as your Git provider
4. Select your `editorial-seo-tool` repository
5. Configure build settings:
   - **Build command**: `echo 'No build step required for static site'`
   - **Publish directory**: `.` (root directory)
   - **Node version**: `18`
6. Click "Deploy site"

## Step 4: Configure Environment Variables

1. In your Netlify dashboard, go to **Site settings** → **Environment variables**
2. Add the following variable:
   - **Key**: `OPENAI_API_KEY`
   - **Value**: Your OpenAI API key
3. Click "Save"

## Step 5: Configure Custom Domain (Optional)

1. In Netlify dashboard, go to **Domain settings**
2. Click "Add custom domain"
3. Enter your domain name
4. Follow the DNS configuration instructions

## Step 6: Enable Automatic Deployments

1. In Netlify dashboard, go to **Site settings** → **Build & deploy**
2. Under "Deploy settings", ensure:
   - **Branch to deploy**: `main`
   - **Build command**: `echo 'No build step required for static site'`
   - **Publish directory**: `.`
3. Under "Deploy hooks", you can create webhooks for manual deployments if needed

## Step 7: Test Your Deployment

1. Visit your Netlify URL (e.g., `https://your-site-name.netlify.app`)
2. Test the application:
   - Open settings and enter your OpenAI API key
   - Create a test article
   - Verify all features work correctly

## Updating the Application

To update your deployed application:

1. Make changes to your local files
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update: describe your changes"
   git push origin main
   ```
3. Netlify will automatically detect the changes and redeploy

## Troubleshooting

### Common Issues

1. **Build fails**: Check that your `netlify.toml` file is in the root directory
2. **Environment variables not working**: Ensure they're set in Netlify dashboard
3. **CORS errors**: Check that your API calls are using HTTPS in production
4. **404 errors**: Verify that your `netlify.toml` redirects are configured correctly

### Support

- **Netlify Docs**: [docs.netlify.com](https://docs.netlify.com)
- **GitHub Docs**: [docs.github.com](https://docs.github.com)
- **OpenAI API Docs**: [platform.openai.com/docs](https://platform.openai.com/docs)

## Security Notes

- Never commit your OpenAI API key to the repository
- Use environment variables for all sensitive data
- The application includes security headers in `netlify.toml`
- All API calls are made client-side (consider server-side implementation for production)

## Performance

- Static assets are cached for 1 year
- The application is optimized for fast loading
- No server-side processing required
- CDN distribution via Netlify
