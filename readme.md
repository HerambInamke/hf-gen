# 🔥 SavageScript

**SavageScript** is a terminal-based AI that roasts your life choices before validating your existence. It's the brutally honest friend you never knew you needed, packaged in a fun CLI experience. This project is currently under construction as part of a mentor-guided journey into the wild world of AI.

---

## 💡 Project Idea

You spill your guts in a single, vulnerable line (e.g., *"I'm a programmer who spends more time debugging than writing new code."*). In return, SavageScript delivers a one-two punch:

* A **savage roast** — so personal it feels like the AI has read your diary.
    > *"So you're a professional typo-fixer? Your code has more red lines than a romance novelist's draft. The only thing you 'ship' is broken software."*
* A **sincere compliment** — to patch up that burn wound with a little bit of love.
    > *"But that persistence is legendary. You have the tenacity of a bulldog trying to solve a Rubik's cube, and that's exactly what makes a great developer."*

It’s designed to be a rollercoaster of emotions, showcasing how AI concepts like Prompting, Structured Output, Function Calling, and RAG can be used to create something genuinely entertaining.

---

## 🧠 Core Concepts Implemented

### 🗣️ Prompting

The soul of SavageScript lies in its meticulously crafted prompts, which give the AI its signature personality. The prompt essentially tells the AI how to behave.

**Example prompt:**
> You are SavageScript, a sharp-witted AI with a heart of gold. Your personality is 90% Gordon Ramsay and 10% Bob Ross. First, deliver a ruthless, soul-crushing roast based on the user's self-description. Be specific, be brutal, but avoid truly offensive topics. Immediately after, pivot to a genuinely warm and uplifting compliment that makes them feel seen and appreciated. Return both in the specified format.

---

### 🧾 Structured Output

To keep the CLI from having a meltdown, the AI's witty banter is neatly packaged into a predictable JSON structure. This ensures we can easily grab the roast and the compliment without parsing a chaotic string.

```json
{
  "roast": "So you're a professional typo-fixer? Your code has more red lines than a romance novelist's draft.",
  "compliment": "But that persistence is legendary. You have the tenacity of a bulldog trying to solve a Rubik's cube, and that's what makes a great developer."
}
```

---

### ⚙️ Function Calling

This is where the AI gets to boss the application around. The model can return metadata suggesting actions for the CLI to perform, making the experience more dynamic and interactive.

**Example:** The AI might feel extra spicy and return:

```json
{
  "roast": "You have the screen time of a teenager and the back pain of a senior citizen. Your posture is a cry for help.",
  "compliment": "Yet, you're incredibly curious and always learning. That hunger for knowledge is something to be proud of.",
  "special_effect": "play_sad_violin"
}
```

The CLI sees the `special_effect` key and can trigger a corresponding function, like displaying a tiny ASCII violin to accompany your shame before the compliment lifts you back up.

---

### 🧠 RAG (Retrieval-Augmented Generation)

RAG is SavageScript's secret weapon—its "comedy cheat sheet." Instead of just making things up, it grounds its responses in a curated vault of premium-grade savagery and kindness.

**How it works:**

1.  **User Confesses:** You describe a tragic detail about yourself.
2.  **Vault Dive:** The system instantly searches its internal knowledge base for similar roasts and compliments related to your input (e.g., "procrastination," "coding," "too many hobbies").
3.  **Inspiration Injection:** These relevant examples are injected into the prompt, giving the AI context and inspiration to generate a burn that’s clever, relevant, and far less generic.
