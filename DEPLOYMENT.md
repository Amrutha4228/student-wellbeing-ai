# 🚀 Deployment Guide - Student Wellbeing AI

## Option 1: Streamlit Cloud (Recommended - Free & Mobile-Friendly)

### Steps:
1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/student-wellbeing-ai.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Set main file: `app.py`
   - Add secrets: `GOOGLE_API_KEY = "your_api_key_here"`
   - Deploy!

3. **Your app will be live at:** `https://yourusername-student-wellbeing-ai-app-xyz.streamlit.app`

## Option 2: Local Network (Laptop + Mobile on same WiFi)

### Run locally and access from mobile:
```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Then access from mobile browser: `http://YOUR_LAPTOP_IP:8501`

## Option 3: Heroku (Alternative Cloud)

### Files needed (already created):
- `requirements.txt` ✅
- `Procfile` (create this):
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

## Mobile Optimization Features Added:
- ✅ Responsive layout with `layout="wide"`
- ✅ Mobile-friendly text area instead of text input
- ✅ Better button sizing with `use_container_width=True`
- ✅ Collapsed sidebar for mobile
- ✅ Error handling for better UX

## Security Note:
For production, use Streamlit secrets instead of .env file:
- Add `GOOGLE_API_KEY` in Streamlit Cloud secrets
- Remove .env from repository (add to .gitignore)