---
title: Announcing HuggingFace Model Support
description: Krypton ML now supports direct HuggingFace model inference
authors: [krypton-team]
tags: [huggingface, release, inference]
---

We're excited to announce that Krypton ML now supports direct HuggingFace model inference in version 0.1.8! This new feature allows you to serve HuggingFace models directly through Krypton ML's simple configuration system, without writing any additional code.

## What's New

You can now serve any HuggingFace model by simply adding it to your `config.yaml`:

```yaml
krypton:
  models:
    - name: gpt2-text-generation
      type: huggingface
      endpoint: /generate
      hf_model_name: gpt2
      hf_task: text-generation
      description: "GPT-2 text generation model"
```

That's it! Krypton ML handles all the model loading and inference setup for you.

## Features

- Support for all HuggingFace model types and tasks
- GPU acceleration with simple device configuration
- Customizable model and generation parameters
- Automatic API endpoint creation
- Built-in error handling and validation

## Getting Started

To use the new HuggingFace support, upgrade to version 0.1.8:

```bash
pip install krypton-ml==0.1.8
```

Here's a complete example configuration showing available options:

```yaml
krypton:
  models:
    - name: text-generation
      type: huggingface
      endpoint: /generate
      hf_model_name: gpt2
      hf_task: text-generation
      hf_model_kwargs:
        torch_dtype: float16
      hf_generation_kwargs:
        max_length: 100
        do_sample: true
      description: "GPT-2 text generation model"
```

## What's Next

This is just the beginning of our HuggingFace integration. We're working on adding support for:
- Fine-tuned model serving
- Model quantization options
- Advanced caching strategies
- More optimization features

Stay tuned for more updates!

## Feedback

We'd love to hear your feedback on the new HuggingFace support. Try it out and let us know what you think on our [GitHub discussions](https://github.com/kryptonhq/krypton-ml/discussions).

Happy model serving! 🚀