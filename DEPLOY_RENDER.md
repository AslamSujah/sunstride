# 🚀 Deploy to Render (FREE Tier + Your $50 Credit)

## ✅ Step 1: Connect GitHub

1. Go to https://render.com
2. Click **"Sign Up"** → Connect with GitHub
3. Authorize Render to access your repositories

---

## ✅ Step 2: Create New Web Service

1. Click **"+ New"** → **"Web Service"**
2. Select **"AslamSujah/sunstride"** repository
3. Configure settings:
   - **Name:** `sunstride`
   - **Region:** `Oregon` (closest, fastest)
   - **Branch:** `main`
   - **Runtime:** `Docker`
   - **Build Command:** (leave empty - auto-detected)
   - **Start Command:** (leave empty - from Dockerfile)

---

## ✅ Step 3: Environment Variables

Add these in Render dashboard:

```
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

---

## ✅ Step 4: Select Plan

- **Free Tier:** Works but goes to sleep after 15 mins of inactivity
- **Starter Plan ($7/month):** Always running + your $50 credit covers ~7 months
- **Recommended:** Click **"Starter"** → Your $50 covers it!

---

## ✅ Step 5: Deploy!

1. Click **"Deploy"**
2. Wait 3-5 minutes for build to complete
3. Your live URL appears: `https://sunstride-xxxx.onrender.com`

---

## 📊 Cost Breakdown (with your $50)

| Plan | Cost | Duration with $50 |
|------|------|------------------|
| Free | $0 | ∞ (but sleeps) |
| Starter | $7/month | 7+ months |
| Standard | $25/month | 2 months |

**Recommendation:** Use **Starter Plan** - your $50 covers 7 months!

---

## 🔧 Troubleshooting

### Build Fails
- Check logs in Render dashboard
- Common: Ollama download timeout
- **Solution:** Increase build timeout to 60 mins in settings

### App crashes after deploy
- Ollama needs time to download Gemma (~2-3 mins)
- **Solution:** App auto-restarts, wait 5 minutes

### Still Failing?
- Open issue: https://github.com/AslamSujah/sunstride/issues
- Include Render build logs

---

## ✨ Your Live App

Once deployed, you can:
- ✅ Share public URL with anyone
- ✅ Use on any device via browser
- ✅ Track usage in Render dashboard
- ✅ See real-time logs

---

## 🎯 Next After Deploy

1. Test your live app
2. Share URL on GitHub issues/discussions
3. Submit to Hacktoberfest!
4. Get contributors!

---

**Ready? Go to https://render.com and click Start! 🚀**
