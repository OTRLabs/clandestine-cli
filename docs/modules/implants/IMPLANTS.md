# Implant Development


## Introduction to Implants as a concept

For the context of the K8Sploit Framework, what I mean by “implant” is basically code that we have managed to land on a target host, and has established a connection back to our C2 server.

For the sake of our project, & because we aiming to allow for advanced agent development: an implant can be anything from a curl command running as a for loop, to an entire malicious package or even entire application crafted around achieving a goal over, potentially a long period of time. 

Open source projects  that would apply to projects such include:

- [Mythic Framework's](https://docs.mythic-c2.net/) [Agents](https://mythicmeta.github.io/overview/)
- [Meterpreter](https://github.com/rapid7/meterpreter) for the [Metasploit Framework](https://github.com/rapid7/metasploit-framework)
- [Empire/starkiller](https://github.com/BC-SECURITY/Starkiller) has a few: 
  + [Sharpire](https://github.com/BC-SECURITY/Sharpire) is  a `C#` example
- Donut

**enterprise options** for implants include:

- [Cobalt Strike](https://www.cobaltstrike.com/resources) Implants
  + [Beacon Object File](https://github.com/ajpc500/BOFs) aggressor scripts?
  
### **Implant Development Goals**
#### **Community Implant Development Goals**:
I intend to design the overall system in a way that is modular and well documented allowing for the easy addition of new implants.


#### **Personal Implant Development Goals**:
I intend to focus on developing one primary `implant` to start. The goal is to develop a highly modular `implant` that is built in a component driven architecture.
The idea is that if you break each feature/functionality of the `implant` can be easily extended with new features, and have old ones rotated out. 

My long term plan is to amass a massive library of these components that can be used to build a variety of different `implants` for different purposes.
You would be able to select the components you want to include in the `implant` before building it.  

primarily with LLVM based languages using Bazel + a  virtual Kubernetes cluster or compose environment that deploys relevant environments required to build binaries for specific implants on specific platforms. 

in addition to LLVM we will have stagers in other languages as well, that can be used to obtain shells such as PHP, JS/TS, etc. 

these stagers primary goal is to 

- assess the current environment
- make efforts  to obtain persistence
- deploy addition payloads to obtain new shells/runtimes/environments with relevant abilities:
    - such as P2P communications (especially with the gleam & elixir implant  runtimes) request routing,
    - & other commands that might be associated with an implant payload
    
    These payload runtimes can be a variety of different environments, which will likely be determined by an information gathering stager, however, the user can choose to specify a payload runtime to deploy. Perhaps in situations where operational security is less critical, you could create a list of your preferred payload runtime to deploy & the stager system goes down the list trying each one until a shell is obtained 
    
    - LLVM based binary
        - C
        - C++
        - Zig
        - Rust
        - Mojo
        - Python?
        - Swift?
        - V?
        - Nim [library](http://library.so) as . Shared objects
        - Go via Go-LLVM
    - Simple Nim module that maybe preforms additional information gathering
    - Powershell scripts
    - Vscode plugins
    - Python app
    - Erlang VM beam
    - Java JVM
    - Java GraalVM
    - Gleam BeamVM

Their capabilities range from a variety of different types of implants. 

## implant arsenal

 ideally to kick things off I am going to begin building out some templates for ideas I have as well as outlining some additional ideas that would be potential rabbit holes or weekend development projects 

- 

deploy

---

 

My goal is to quickly build a fairly simple post exploitation framework within the existing system 

---

---

---

---

# Developing Implants:

## Features & Functionality:

Big picture, we want to have a variety of agents with a fairly standard set of features & capabilities, as well as additional unique capabilities to make the implant more interesting, 

If I am going to be developing these agents, I want to do the bare minimum in that I intend to avoid developing systems that interfere with regular operations of business. 

This means:

- no ransomware adjacent implants (file encryption) (not even for “demonstration purposes”, too easy to potentially repurpose the base codebase into something destructive

- No file manipulation beyond exfiltrating copied data.
- No manipulation of existing user accounts

All in all things can be summarized as:

- the goal is to keep a low profile
- Use stagers to slowly gather information & deploy the proper stage & payload runtime
- establish persistence in a quiet manner. Try and obtain access to existing user accounts rather than making new ones on infected hosts. I would recommend checking logs to estimate when they may change the password (see if organization who owns the machine enforces regular password changes to built a f“estimated time with access to machine remaining: {time_left}” based on the intervals of passwords being reset or last datetime that logs on the infected host begin at, combined with uptime and other environmental factors to create a system that makes better and better guesses of time remaining over time using SurrealDB functions + SurrealML
- 
- Check when logs were cleared to try and determine whether they would likely be  wiping things or following any standard for best practices & IT infrastructure hygiene

The goal is to approach implant development with the desire to build modular systems where individual components are optional and only included in implant builds they are needed for. (For example, a specific communication protocol can be excluded from a build.) 

This “module” style development with a focus on LLVM applications for implants allows us to stay one step ahead in terms of evasion by allowing us to identify problematic parts of code that are causing it to be flagged as malicious through a series of automated static & dynamic analysis tests

The overall focus on maintaining the agent as a module based highly swappable & unique experience minimizes the risk of… a lot of things but generally gives the operator more control over the impact on infected machines, and allows operators to maintain access to TTPs and keep them private while preforming research & testing or other legitimate operations (im sure Zerodium does not want their code public)

We will have a reinstall feature for if: 

- you want to include a new feature
- You want to downsize the implant on the infected host to minimize footprint for periods of hibernation

# zig build system accessible via API

This zig based build system allows for enhanced evasion by using a variety of implementations of the same general LLVM functions, just in different languages or designed differently.

Ideally, you would be able to provide a “build config” for lack of better words describing the type of binary implant you are looking to walk away with using a standardized JSON format 

This would generate a one time fully unique configuration for the build using a series of both randomized & controlled variables that are used to create a unique build of the agent based on the tools available in that iteration. So there would be a list of functions that all preform some version of the same functionality to return the same data, then inject some obfuscation and do this for each function, implementing a variety of different methods to build each “feature” of the implant 

These functions are selected at build time based on target machines system architecture and the compatible functionality that the repository containing the multiple implementations of the functions for the agent has available 

We need to figure out a compatibility management system that is responsive within the UI 

Like I want select fields of incompatible modules to be “greyed out” in the ui if we don’t have a file compatible with other selections 

Pivoting is a primary focus 

- overseeer feature includes a graph canvas node view similar to surrealist by SurrealDB, or Node Red, or neo4j graphs, providing a look into the connections each host has the ability to make. The end goal is an ever growing map of the internet including internal network connections that we can access
- 

 I believe that developing Implants that directly disrupt the flow of day to day business operations is beyond unethical. I don’t see a reason 

Honestly I think it is more fun & there is more sport in co-existing and trying to maintain access for as long as possible without detection. 

- exfiltrating sensitive information, aiming for a comprehensive report on all information found & analyzed on services within a particular target scope.
- Subtly making use of infected hosts via botnet style command orchestration.
- use of a wide variety of different stealthy protocols for communications

## modular “as needed” approach to implant features

basically rather than burning my TTPs (LOL as if I have something special here), I intend to build only the required functionality into implants, ideally giving them the ability to “pull down” more functionality from CDN style servers or git or some shit idk I mean there’s a million options. But if needed we can use internal servers via a special cluster for idk a CDN if operations are getting large 

- using an advanced builder (zig?) + information from:
    - current engagements state & information related to targets.
    - similar information for prior engagements

- communications between implants & the C2 are divided up across a series of different protocols, each designed to transmit a specific type of data back to the C2 based on a series of parameters, we assess the information we are trying to send back to the user

Basically the idea is to add as many or as few components to the agent before you build it. Similar to Mythic, we will have a UI that clearly asks you, what OS are you looking to target, what implant, then add features to the implant using a multi select form 

### **Decoy Traffic Functionality**
Used to obfuscate actual communications between the `implant` & the `C2`
#### Example Protocols:
- Noisy socket (for obfuscation & evasion / general noise to logs)
- white noises research in a browser
  + browsing google/bing for random things 

### **Heartbeat Protocols**
for Pinging
#### Example Protocols:
- ICMP
- HTTP(S)
- DNS

- Message Passing Protocols 
Used More Detailed Status reports from implant.


- command list refresh (return json data)
    - Tox
    - Signal
    - Oblivious HTTP
    - Email?
    - Noisy sockets 
    - Tor
    - Matrix
    - Email over tor (salmon SMTP client lib + Stem by Tor project to access SMTP services like postfix over tor)
    - XMPP
- Small rapid file transfers:
    - HTTPS
    - Websocket
    - Tox
    - Telegram bot
- Large slow file transfers:
    - Tox
    - I2P?
    - IPFS
    - Bittorrent
    - Telegram bots
    - Onionshare
    - 
- Mass file transfer
    - Telegram bot
    - Email over Tor?
    
    -