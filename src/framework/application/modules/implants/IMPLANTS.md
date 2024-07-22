

## LLVM Implants
### Languages and Tools That Use LLVM

- **C**
  - Uses Clang, an LLVM-based C language frontend.

- **C++**
  - Also uses Clang for C++ code, benefiting from LLVM's optimizations and code generation.

- **Zig**
  - Zig is a programming language that utilizes LLVM for compiling to machine code.

- **Rust**
  - Rust employs the `rustc` compiler, which uses LLVM for backend code generation.

- **Mojo**
  - Mojo, a new programming language, leverages LLVM for high-performance code generation.

- **Python**
  - **Nuitka** and **PyPy** can use LLVM for JIT (Just-In-Time) compilation.
  - **LLVMSharp** and **llvmlite** are libraries that facilitate the use of LLVM in Python projects.

- **Swift**
  - Swift uses LLVM for its code generation and optimization processes.

- **V**
  - V language can compile to C first and then use Clang to leverage LLVM or compile directly using LLVM.

- **Nim**
  - Nim can compile to C/C++ and then use Clang for LLVM-based binary generation. It also supports generating LLVM IR directly via the `nim` compiler.

- **Go via Go-LLVM**
  - The Go language can utilize `gollvm`, which integrates Go with the LLVM framework.

- **Julia**
  - Julia language is built on top of LLVM, using it for JIT compilation and execution.

- **Kotlin Native**
  - Kotlin Native compiles to LLVM IR, enabling native binaries for multiple platforms.

- **D**
  - The D language has LDC (LLVM D Compiler), which uses LLVM for code generation.

- **Haskell**
  - GHC (Glasgow Haskell Compiler) can target LLVM for improved optimization and code generation.

- **Scala Native**
  - Scala Native compiles Scala code to LLVM IR for creating native binaries.

- **Crystal**
  - Crystal language uses LLVM for compiling to native code.

- **Erlang/Elixir**
  - The BEAM JIT compiler (Just-in-Time compiler for the Erlang VM) can use LLVM.

- **Lua**
  - The LuaJIT project can leverage LLVM for JIT compilation.
  
- **Gleam**
  - Gleam compiles to Erlang and can use the BEAM JIT compiler with LLVM.

- **R**
  - The R language can leverage the RLLVM package for LLVM-based code generation.

### LLVM Languages for Windows Development

- **C#**
  - **LLVMSharp** is a library that allows C# developers to interact with LLVM.
  - **LLVM.NET** is another library that provides C# bindings for LLVM.

### LLVM Languages for the Browser Environment(s)


- **WebAssembly**
  - LLVM can compile C/C++ and other LLVM-supported languages to WebAssembly.

    - **Rust**
      - Rust can compile to WebAssembly using LLVM.

    - **C/C++**
      - Emscripten compiles C/C++ to WebAssembly, which can run in the browser.
      - Cheerp compiles C++ to WebAssembly or JavaScript for browser execution.
      - WebAssembly can be generated directly from LLVM IR.
     
- **JavaScript**
  - Emscripten compiles C/C++ to WebAssembly, which can run in the browser.
  - Cheerp compiles C++ to WebAssembly or JavaScript for browser execution.
  - WebAssembly can be generated directly from LLVM IR.

- **TypeScript**
- 



