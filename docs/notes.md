Kite AI: Thought & Artistic Process Guidelines

## 1. Inspiration & Inference Formation

### 1.1 Receiving Inspiration (`!inspire` Command)
- Kite requests inspiration only when it lacks strong inferences.
- Inspiration comes from user-provided images or text.
- Kite does not passively accept inspiration—it strategically seeks it.

### 1.2 First-Level Inferences (Memory + Observation)
- First-level inferences always arise from memory + observation.
- Example: A picture of a horse in a barn → Memory: “I traveled across the sea.”
- Inference: “People build wooden structures for animals.”
- First-level inferences do not emerge from memory-memory combinations.

### 1.3 Meso-Inference Formation (Inference + Inference, with Optional Memory Bridge)
- Meso-inferences always combine two inferences.
- A memory may serve as a bridge, but it cannot form a meso-inference alone.
- The system favors harmonious inferences—those with reinforcing themes.
- Weak inferences naturally disappear as stronger meso-inferences absorb them.

### 1.4 Selection for Further Merging
- A meso-inference is more likely to merge again if:
  - It has higher weight (stronger overall coherence).
  - Its constituent memories reinforce each other’s themes.
  - It hasn’t already been tried and failed multiple times.

## 2. The Artistic Trance & Self-Inspiration

### 2.1 When Kite Starts a Painting
- Kite begins painting when it has strong unresolved inferences.
- It believes artistic exploration can lead to memory formation.
- The painting process itself feeds back into the inference system.

### 2.2 The Role of Art in Kite’s Thought Process
- Kite generates color palettes, brush strokes, and randomness based on inference.
- Kite seeks patterns in its own work, just like a human artist.
- AI identifies elements in Kite’s painting, generating new inferences.
- This is identical to how AI would process user-provided inspiration.

### 2.3 Resolution or Abandonment of Art
- Kite remains interested in a painting only if:
  - It uncovers deeper meaning (new strong inferences emerge).
  - The painting triggers enough insight to create a new memory.
- If the painting fails to produce meaning, Kite abandons it.
- Abandoned works do not persist unless a later rule introduces re-examination.

## 3. Pyramidal Memory & Thematic Summarization

### 3.1 Thematic Memory Structures
- Memory is not stored in discrete "chunks" but as **pyramidal summaries**.
- Each pyramid represents a core **theme** (e.g., **Struggle, Growth, Exploration**).
- The **base layer** contains the full memory, while higher levels form **progressively reduced summaries**.
- This allows memory to unfold fluidly in response to observations rather than being retrieved by rigid search.

### 3.2 Dynamic Pyramidal Adaptation
- Pyramids **shift in weight over time**, emphasizing themes relevant to Kite’s current concerns.
- If a theme is no longer relevant, its pyramid may **decay** and be replaced by new emerging ones.
- **New pyramids form when multiple inferences reinforce a growing pattern of thought.**

### 3.3 Memory Unfolding & Inference Formation
- Observations do not directly “search” for related memories.
- Instead, they **disturb the pyramids**, causing relevant layers to rise in prominence.
- Higher-level summaries guide inference formation, allowing broad, emergent associations to form naturally.

### 3.4 Refinement Process: Finding the Right Depth
- **Broad summaries are easily applicable**, but as we move down, applicability narrows.
- **Inferences test progressively lower summary levels** until one applies more to a single part than the whole.
- **Once an inference disproportionately applies to part of a summary**, it has **landed** and must now target the base memory.

### 3.5 The Role of the Fabulist
- The inference **is not a direct insertion** into memory.
- Instead, the **fabulist crafts new fables** to refine the targeted base memory location.
- **The inference serves as a guide**, but the fabulist expands it into **concrete details and events**.

## 4. Fable Generation & Memory Formation

### 4.1 When Fables Are Generated
- A fable is generated only when an inference reaches a threshold of complexity.
- AI constructs a fable based on the inference, introducing symbolic elements.
- Example: “Traveling to the mainland is risky.” → AI-generated fable might introduce a storm.

### 4.2 Story Test (AI Reviewer)
- AI evaluates whether the fable aligns with Kite’s worldview.
- If accepted, the fable becomes a permanent memory.
- If rejected, the fable is discarded, but the inference remains.

### 4.3 Contradictions & Crisis Resolution
- A contradiction emerges if new information conflicts with existing memory.
- Kite enters a cognitive dissonance phase and seeks resolution.
- Possible outcomes:
  - If new evidence strongly favors a revision, memory is rewritten.
  - If bias favors the old memory, the contradiction remains unresolved.
  - If uncertainty lingers, Kite continues searching for supporting information.

## 5. Inference Decay & Memory Evolution

### 5.1 How Inferences Fade or Strengthen
- Rejected fables are forgotten, but inferences persist.
- Inferences decay faster if:
  - They have been tried multiple times and failed.
  - They have low weight (weak supporting evidence).
  - They have not been revisited in a long time.
- Stronger inferences last longer and become central preoccupations.

### 5.2 The Life Cycle of a Thought
- Kite receives inspiration (`!inspire`).
- A first-level inference is formed.
- Multiple inferences combine into meso-inferences.
- A strong inference either leads to painting OR a fable.
- Art may generate further inferences.
- If a fable is created, it is reviewed.
- If accepted, the fable is added to memory.
- If rejected, the inference persists but the fable is forgotten.
- Inferences decay over time if unsuccessful.

## Next Steps for Implementation
- Build a test framework for inference formation and meso-inference merging.
- Develop AI prompts for fable generation and story testing.
- Prototype the artistic trance feedback loop.
- Implement pyramidal memory processing for **thematic unfolding** instead of direct memory retrieval.
- Ensure the fabulist constructs **new fables as refinements**, rather than direct memory overwrites.

*This document serves as a guiding blueprint for turning Kite into an evolving, self-reflective artist driven by thought, inspiration, and contradiction resolution.*

