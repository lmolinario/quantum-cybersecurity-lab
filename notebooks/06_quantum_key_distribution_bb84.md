# 06 - Quantum Key Distribution and BB84

This note introduces Quantum Key Distribution (QKD) and the BB84 protocol from a cybersecurity-oriented perspective.

## 1. What Is Quantum Key Distribution?

Quantum Key Distribution is a family of protocols used to establish shared secret keys using quantum communication principles.

QKD does not encrypt data directly.

It helps two parties establish a shared key that can later be used with classical symmetric encryption.

## 2. BB84 Overview

BB84 is one of the earliest and most famous QKD protocols.

It was proposed by Charles Bennett and Gilles Brassard in 1984.

The main idea is to encode bits into quantum states using different bases.

## 3. Basic Actors

Traditional explanations use three actors:

- Alice: sender
- Bob: receiver
- Eve: potential eavesdropper

Alice sends quantum states to Bob.

Bob measures them using randomly chosen bases.

Alice and Bob later compare bases over a public classical channel and keep only the compatible measurements.

## 4. Simplified BB84 Flow

```text
1. Alice generates random bits
2. Alice chooses random bases
3. Alice encodes bits into quantum states
4. Bob chooses random measurement bases
5. Bob measures the received states
6. Alice and Bob compare bases publicly
7. They discard incompatible measurements
8. They estimate the error rate
9. If the error rate is acceptable, they derive a shared key
```

## 5. Why Eavesdropping Can Be Detected

In quantum mechanics, measuring an unknown quantum state can disturb it.

If Eve intercepts and measures the quantum states, she may introduce detectable errors.

This allows Alice and Bob to estimate whether the channel has been disturbed.

## 6. QKD vs Post-Quantum Cryptography

QKD and Post-Quantum Cryptography are different approaches.

QKD requires specialized quantum communication infrastructure.

Post-Quantum Cryptography is based on classical algorithms designed to resist quantum attacks.

## 7. Cybersecurity Interpretation

QKD is important from a theoretical and high-security communication perspective.

However, for most real-world systems, Post-Quantum Cryptography is currently the more practical migration path because it can be deployed in classical networks and software systems.

## 8. Key Takeaways

- QKD helps establish shared keys.
- BB84 uses quantum states and random bases.
- Eavesdropping can introduce detectable errors.
- QKD requires specialized infrastructure.
- QKD and Post-Quantum Cryptography are not the same thing.
