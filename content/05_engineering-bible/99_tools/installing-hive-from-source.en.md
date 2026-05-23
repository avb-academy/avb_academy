---
title: "Build Hive from Source for Arch Linux"
date: 2020-05-19
weight: 1
---

{{% notice info %}}
This is both a collection of instructions from the associated repositories along with solutions/workarounds for common pitfalls during installation.  
This tutorial was written with Arch Linux version 7.0.5-arch1-1.
{{% /notice %}}

We will be installing all repositories to the home directory `~/` to maintain consistency.

Before starting, ensure you have updated your package manager:

```bash
sudo pacman -Syu
```

If you have not done so, install the `base-devel` package to install important dependencies such as `gcc`, `make`, `makepkg`, and other very important dependencies:

```bash
sudo pacman -S --needed base-devel
```

Also ensure you have `git`:

```bash
sudo pacman -S git
```

---

## AVDECC

Repository: https://github.com/L-Acoustics/avdecc

### Requirements

- **CMake 3.29+**
  ```bash
  sudo pacman -S cmake
  ```
- **C++17 compliant compiler** — `g++` v11.0 or greater (covered by `base-devel`)
  ```bash
  sudo pacman -S gcc
  # Check version with:
  g++ -v
  ```
  The last line will show the version number (`gcc version 16.1.1 20260430 (GCC)` in this example):  
  ```bash
  g++ -v
  Using built-in specs.
  COLLECT_GCC=g++
  COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-pc-linux-gnu/16.1.1/lto-wrapper
  Target: x86_64-pc-linux-gnu
  Configured with: /build/gcc/src/gcc/configure --enable-languages=ada,c,c++,d,fortran,go,lto,m2,objc,obj-c++,rust,cobol --enable-bootstrap --prefix=/usr --libdir=/usr/lib --libexecdir=/usr/lib --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=https://gitlab.archlinux.org/archlinux/packaging/packages/gcc/-/issues --with-build-config=bootstrap-lto --with-linker-hash-style=gnu --with-system-zlib --enable-cet=auto --enable-checking=release --enable-clocale=gnu --enable-default-pie --enable-default-ssp --enable-gnu-indirect-function --enable-gnu-unique-object --enable-libstdcxx-backtrace --enable-link-serialization=1 --enable-linker-build-id --enable-lto --enable-multilib --enable-plugin --enable-shared --enable-threads=posix --disable-libssp --disable-libstdcxx-pch --disable-werror --disable-fixincludes
  Thread model: posix
  Supported LTO compression algorithms: zlib zstd
  gcc version 16.1.1 20260430 (GCC)
  ```

- **Make** (covered by `base-devel`)

- **pcap developer package**
  ```bash
  sudo pacman -S libpcap
  ```
- **ncurses developer package** *(optional, required to run for examples)*
   ```bash
  sudo pacman -S ncurses
  ```

### Steps

1. Clone the repository and cd into it:
   ```bash
   git clone https://github.com/L-Acoustics/avdecc.git
   cd avdecc
   ```

2. Checkout a stable release branch:
   Find releases at: https://github.com/L-Acoustics/avdecc/releases

   For example, release `v4.3.1.1` has tag `v4.3.1.1` and commit hash `6d61a92`:
   ```bash
   git checkout 6d61a92
   ```

3. Update submodules:
   ```bash
   git submodule update --init --recursive
   ```

4. Run the provided `gen_cmake.sh` script with `-release`:
   ```bash
   ./gen_cmake.sh -release
   ```

5. Go into the generated output folder:
   ```bash
   cd ~/avdecc/_build_linux_x64_makefiles_release
   ```

6. Compile:
   ```bash
   make
   ```

---

## HIVE

Repository: https://github.com/christophe-calmejane/hive

### Requirements

- **CMake 3.29** (already installed from `base-devel` and AVDECC installation)

- **Qt 6.8.3** — Install via the Qt online installer. Installing the `qt6-base-dev` package can cause build issues.
  Follow instructions here: https://doc.qt.io/qt-6/qt-online-installation.html
  Take note of the install path for later. In this example it is in `~/qt/`.

  **Note:** When you download the installer, you will need to set it as executable:
  ```bash
  chmod +x qt-online-installer-linux-x64-4.11.0.run
  ```

  {{% notice caution %}}
  Make sure to install the correct Qt version: 6.8.3.  
  The version must be selected in the manual install. 
  {{% /notice %}}

  ![Qt manual installation step 1](/images/hive-qt-install1.png)
  ![Qt manual installation step 2](/images/hive-qt-install2.png)

- **g++ 11.0**
  AUR package: https://aur.archlinux.org/packages/gcc11

  You can either install g++ 11.0 manually or with yay

  1. Installing manually:
  ```bash
  git clone https://aur.archlinux.org/gcc11.git
  cd gcc11
  makepkg -si
  ```

  2. Installing via `yay`:

  Optional: Install yay:

  ```bash
  git clone https://aur.archlinux.org/yay-bin.git
  cd yay-bin
  makepkg -si
  ```

  ```bash
  yay -s gcc11
  ```

  2.1 The installation process asks you which packages to install:
  ```bash
  9 aur/matlab-r2025b-gcc11-meta R2026a-1 (+0 0.00) 
    A high-level language for numerical computation and visualization (R2025b, GCC11, meta)
  8 aur/matlab-r2025a-gcc11-meta R2026a-1 (+0 0.00) 
      A high-level language for numerical computation and visualization (R2025a, GCC11, meta)
  7 aur/matlab-r2024b-gcc11-meta R2026a-1 (+0 0.00) 
      A high-level language for numerical computation and visualization (R2024b, GCC11, meta)
  6 aur/matlab-r2024a-gcc11-meta R2026a-1 (+0 0.00) 
      A high-level language for numerical computation and visualization (R2024a, GCC11, meta)
  5 aur/matlab-r2023b-gcc11-meta R2026a-1 (+0 0.00) 
      A high-level language for numerical computation and visualization (R2023b, GCC11, meta)
  4 aur/matlab-gcc11-meta R2026a-1 (+0 0.00) 
      A high-level language for numerical computation and visualization (GCC11, meta)
  3 aur/gcc11-fortran 11.5.0-1 (+6 0.49) 
      Fortran front-end for GCC (11.x.x)
  2 aur/gcc11-libs 11.5.0-1 (+6 0.49) 
      Runtime libraries shipped by GCC (11.x.x)
  1 aur/gcc11 11.5.0-1 (+6 0.49) 
      The GNU Compiler Collection - C and C++ frontends (11.x.x)
  ==> Packages to install (eg: 1 2 3, 1-3 or ^4)
  ==> 
  ```
  
  Select `1`.

  2.2 Then you are asked whether you want to clean build
  ```bash
  ==> Packages to cleanBuild?
  ==> [N]one [A]ll [Ab]ort [I]nstalled [No]tInstalled or (1 2 3, 1-3, ^4)
  ==> 
  ```

  Select `A`

  2.3 Then you are asked if you want to show any diffs:

  ```bash
  ==> Diffs to show?
  ==> [N]one [A]ll [Ab]ort [I]nstalled [No]tInstalled or (1 2 3, 1-3, ^4)
  ==> 
  ```

  Select `N`.

  2.4 Then you are asked if you want to remove the make dependencies after install:
  ```bash
  :: Remove make dependencies after install? [y/N]
  ```

  Select `N`

  {{% notice info %}}
  Installing GCC11 may take time. If you run into any issues, start with rerunning `sudo pacman -Syu`.
  {{% /notice %}}

### Steps

1. Clone the repository and cd into it:
   ```bash
   git clone https://github.com/christophe-calmejane/Hive.git
   cd Hive
   ```

2. Checkout a stable release:
   Find releases at: https://github.com/christophe-calmejane/Hive/releases

   Locate the tag/version-number and commit hash. For example, release `v1.4.0` has tag `v1.4.0` and commit hash `0d28c27`:
   ```bash
   git checkout 0d28c27
   ```

3. Copy `.hive_config.sample` to `.hive_config`, then edit it for installer customization:
   ```bash
   cp .hive_config.sample .hive_config
   ```

4. Initialize git submodules
   ```bash
   git submodule update --init --recursive
   ```
   Then check the status:
   ```bash
   git status
   ```

   You may need to perform a `git reset` inside some submodules (e.g. `3rdparty/sparkleHelper`). If you see an output like this from `git status`:

   ```
   ➜  Hive git:(v1.4.0) git status
   HEAD detached at v1.4.0
   Changes not staged for commit:
     (commit or discard the untracked or modified content in submodules)
       modified:   3rdparty/sparkleHelper (modified content)
   ```

   Run the following to fix it:
   ```bash
   cd ~/Hive/.git/modules/3rdparty/sparkleHelper
   git reset HEAD --hard
   ```

5. Run the setup script to set up your working copy:
   ```bash
   ./setup_fresh_env.sh
   ```

6. Set environment variables before running `gen_cmake.sh`:
   ```bash
   # Set the compilers
   export CC=gcc-11
   export CXX=g++-11
   # Set the Qt 6.8 path so CMake finds it first
   export CMAKE_PREFIX_PATH=~/Qt/6.8.3/gcc_64
   ```

7. Run the cmake generation command:
   ```bash
   ./gen_cmake.sh -release -qtdir ~/Qt/6.8.3/gcc_64/lib/cmake -qtvers 6.8.3 -- -DCMAKE_POLICY_VERSION_MINIMUM=3.5
   ```

   {{% notice info %}}
   - **Note 1:** The `-qtdir` parameter should be the location of your Qt directory. In this example, Qt was installed to the home directory.
   - **Note 2:** Run `gen_cmake.sh -h` to display the help menu.
   - **Important:** If you are using CMake >= 4.0, you must add this extra parameter: `-- -DCMAKE_POLICY_VERSION_MINIMUM=3.5`
   {{% /notice %}}

8. Go into the generated output folder:
   ```bash
   cd ~/Hive/_build_linux_x64_makefiles_release/
   ```

9. Compile everything:
   ```bash
   cmake --build .
   ```

The Hive binary will be located at:
```
~/Hive/_build_linux_x64_makefiles_release/src/Hive
```
Create a symlink in PATH
```
sudo ln -s ~/Hive/_build_linux_x64_makefiles_release/src/Hive /usr/local/bin/Hive
```

You are now able to run Hive from the terminal by typing `Hive`.

---

## Running Hive

> **Important:** Before running the Hive binary on Linux, you must grant the program access to raw socket creation:

```bash
sudo setcap cap_net_raw+ep ~/Hive/_build_linux_x64_makefiles_release/src/Hive
```

Then run the Hive binary:

```bash
sudo Hive
```
