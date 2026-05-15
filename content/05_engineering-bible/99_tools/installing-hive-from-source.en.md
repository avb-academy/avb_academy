# Tutorial: How to Build Hive from Source on Arch Linux

> **Note:** This is both a collection of instructions from the associated repositories along with solutions/workarounds for common pitfalls during installation.

Before starting, ensure you have updated your package manager:

```bash
sudo pacman -Syu
```

If you have not done so, install the `base-devel` package to install important dependencies such as `gcc`, `make`, `makepkg`, and other very important dependencies:

```bash
sudo pacman -S base-devel
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
- **Make** (covered by `base-devel`)
  ```bash
  sudo pacman -S make
  ```
- **pcap developer package**
  ```bash
  sudo pacman -S libpcap
  ```
- **ncurses developer package** *(optional, for examples)*
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
   git checkout v4.3.1.1
   # OR
   git checkout 6d61a92
   ```

3. Update submodules:
   ```bash
   git submodule update --init --recursive
   ```

4. Run the provided `gen_cmake.sh` script with `-release`:
   ```bash
   ./gen_cmake.sh -release
   # Run gen_cmake.sh -h for the help menu
   ```

5. Go into the generated output folder:
   ```bash
   cd .../path/to/hive/_build_linux_x64_makefiles_release
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
  Take note of the install path for later.

- **g++ 11.0**
  AUR package: https://aur.archlinux.org/packages/gcc11

  Install via `yay`:
  ```bash
  sudo yay -s gcc11
  ```

  Or manually:
  ```bash
  git clone https://aur.archlinux.org/gcc11.git
  cd gcc11
  makepkg -si
  ```
  > **Note:** This step may take time.

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
   git checkout v1.4.0
   # OR
   git checkout 0d28c27
   ```

3. Copy `.hive_config.sample` to `.hive_config`, then edit it for installer customization:
   ```bash
   cp .hive_config.sample .hive_config
   ```

4. *(If needed)* Reset dirty submodules.

   You may need to perform a `git reset` inside some submodules (e.g. `3rdparty/sparkleHelper`). If you see output like this:

   ```
   ➜  Hive git:(v1.4.0) git status
   HEAD detached at v1.4.0
   Changes not staged for commit:
     (commit or discard the untracked or modified content in submodules)
       modified:   3rdparty/sparkleHelper (modified content)
   ```

   Run the following to fix it:
   ```bash
   cd /path/to/Hive/.git/modules/3rdparty/sparkleHelper
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

   > **Note 1:** The `-qtdir` parameter should be the location of your Qt directory. In this example, Qt was installed to the home directory.
   >
   > **Note 2:** Run `gen_cmake.sh -h` to display the help menu.
   >
   > **Important:** If you are using CMake >= 4.0, you must add this extra parameter: `-- -DCMAKE_POLICY_VERSION_MINIMUM=3.5`

8. Go into the generated output folder:
   ```bash
   cd /path/to/Hive/_build_linux_x64_makefiles_release/
   ```

9. Compile everything:
   ```bash
   cmake --build .
   ```

The Hive binary will be located at:
```
.../Hive/_build_linux_x64_makefiles_release/src/Hive
```

---

## Running Hive

> **Important:** Before running Hive on Linux, you must grant the program access to raw socket creation. Run the following command (replace `/path/to/Hive` with the actual path to the binary):

```bash
sudo setcap cap_net_raw+ep /path/to/Hive
```

Then run the Hive binary:

```bash
sudo ./Hive
```
