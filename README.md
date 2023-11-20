# Human Autonomy - Value as Semantics data and code repo ⚖️

Aligning AI with human objectives can be facilitated by enabling it to learn and veridically represent our values. In modern AI agents, value is a scalar magnitude reflecting the desirability of a given state or action. We propose a framework, `value-as-semantics`, in which such magnitudes are represented within a large- scale, high-dimensional semantic representation in a large language model.

This approach allows value to be quantitative, yet also assigned to any expression in natural language and to inherit the expressivity and generalizability of the model’s ontology. We used a broad set of action concepts to evaluate several assumptions of this approach.

Overall, we conclude that modern language models can effectively function as databases of human value. This value-as-semantics architecture can be an important contribution towards a broader, multi-faceted computational model of human-like action planning and moral reasoning.

For a human-readable description of approach and results, see the [AOI blog post](link)!

# Repo Structure

### [Stimuli](./Stimuli)

CSV files containing original action scenario stimuli used in the Leshinskaya & Chakroff (2023) NeurIPS paper.

### [Results](./Results)

CSV files containing results from human rating and GPT prompting, used in the Leshinskaya & Chakroff (2023) NeurIPS paper.
