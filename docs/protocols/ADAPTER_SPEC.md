# Graphify Adapter Specification

**Protocol:** Universal AI Context Protocol (UACP)

**Document:** Adapter Specification

**Version:** 1.0

**Status:** Stable

**Applies To:** All Graphify Adapter Implementations

---

# 1. Purpose

An adapter is the component responsible for converting AI-specific context into the Universal AI Context Protocol (UACP).

Every supported AI system communicates differently. The purpose of an adapter is to normalize those differences while preserving the original meaning of the project context.

Adapters are the only components allowed to understand AI-specific formats.

Everything after an adapter operates exclusively on UACP.

---

# 2. Design Philosophy

Graphify never translates directly between AI systems.

Correct architecture:

AI System

↓

Adapter

↓

UACP

↓

Validation

↓

Capability Negotiation

↓

Translation

↓

Destination AI

Incorrect architecture:

AI System

↓

Another AI System

Direct AI-to-AI translation is prohibited because it creates maintenance complexity and prevents protocol standardization.

---

# 3. Responsibilities

Every adapter MUST:

* Read context from exactly one AI format.
* Convert that context into valid UACP.
* Preserve project meaning.
* Preserve project identity.
* Preserve project history whenever available.
* Preserve project decisions whenever available.
* Produce deterministic output.
* Produce protocol-compliant metadata.

---

# 4. Non-Responsibilities

Adapters MUST NOT:

* Perform translation between AI systems.
* Modify project meaning.
* Invent project information.
* Remove mandatory UACP sections.
* Skip validation.
* Negotiate capabilities.
* Execute business logic unrelated to protocol conversion.

---

# 5. Required Output

Every adapter must generate a valid UACP object.

At minimum the output must contain:

* protocol
* metadata
* identity
* history
* decisions
* reconstruction
* continuation
* quality

The adapter is responsible for mapping AI-specific fields into these standard sections.

---

# 6. Metadata Requirements

Every adapter must provide metadata describing the source.

Minimum metadata:

* adapter
* source_ai
* schema_version
* generated_by

Example:

adapter: chatgpt

source_ai: ChatGPT

schema_version: 1.0

generated_by: Graphify

---

# 7. Stateless Design

Adapters should be stateless.

An adapter should produce identical UACP output when given identical input.

Adapters should not depend on global variables or previously translated sessions.

---

# 8. Validation

Adapters do not determine whether output is valid.

Instead, every generated UACP document must be passed to the protocol validator before translation.

Validation remains a separate protocol stage.

---

# 9. Capability Independence

Adapters should describe the originating AI only.

Capability comparison belongs to the Capability Negotiation Engine.

Adapters must not make assumptions about the destination AI.

---

# 10. Error Handling

Adapters should report failures clearly.

Typical errors include:

* Unsupported schema
* Missing mandatory fields
* Invalid AI response
* Corrupted context
* Unsupported protocol version

Adapters should never silently discard information.

---

# 11. Extensibility

New AI systems may be added without changing existing adapters.

Each new AI requires exactly one adapter.

Example:

ChatGPT

↓

ChatGPT Adapter

↓

UACP

Claude

↓

Claude Adapter

↓

UACP

Gemini

↓

Gemini Adapter

↓

UACP

DeepSeek

↓

DeepSeek Adapter

↓

UACP

The protocol architecture ensures that adding a new AI never requires modifying previously implemented adapters.

---

# 12. Compatibility

Adapters should support backward-compatible protocol versions whenever practical.

If an adapter cannot support a protocol version, it should clearly report the incompatibility rather than generating invalid UACP.

---

# 13. Testing Requirements

Every adapter implementation should be tested for:

* Successful protocol generation
* Correct metadata generation
* Deterministic output
* Protocol validation compatibility
* Error handling
* Version compatibility

---

# 14. Future Evolution

Future adapter implementations may support:

* Streaming context conversion
* Incremental context updates
* Partial protocol generation
* Multi-session reconstruction
* Distributed AI synchronization

These extensions must remain compatible with the core adapter responsibilities defined in this specification.

---

# 15. Summary

Adapters are responsible only for converting AI-specific context into the Universal AI Context Protocol.

They isolate platform-specific differences while preserving project understanding.

Every Graphify implementation, regardless of programming language, should follow this specification to ensure interoperability across all AI systems.
