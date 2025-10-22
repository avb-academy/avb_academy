# AVB Academy

AVB Academy is a knowledge base dedicated to Milan AVB, focusing on providing detailed and reliable resources about the Milan protocol and its applications in Audio Video Bridging (AVB) networks.

Please check out the website under https://avb-academy.com for the full experience.

## Table of Contents

- [Introduction](#introduction)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Contact and Support](#contact-and-support)

## Introduction

AVB Academy is an online resource designed to help users understand the Milan protocol and its role in AVB networks. It provides a comprehensive glossary, detailed explanations of AVB concepts, and other educational materials.

This website is not affiliated with Avnu or any other organizations involved in Milan standardization; it represents a personal project.

## Install Instructions

To set up the AVB Academy locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone --recurse-submodules https://github.com/avb-academy/avb_academy.git
   cd avb-academy
   ```
2. Install Hugo: https://gohugo.io/installation/
3. Run the build script for images  
    ```bash 
    ./build.sh --images
    ```
4. Run the hugo server locally
    ```bash
    hugo server
    ```
5. Open your browser and go to http://localhost:1313 to view the site.

## Usage

AVB Academy offers various features to help users learn about Milan AVB:

- **Glossary**: A searchable glossary that includes terms and detailed descriptions.
- **Tooltips**: Glossary terms are highlighted and provide tooltips for quick explanations.
- **Search Functionality**: Easily find terms, articles, or documentation.
- **Termbase**: A yaml based dictionary for automatic translation of technical terms.

## Contributing

Contributions very welcome! If you'd like to help improve AVB Academy, you can:

1. Fork the repository and clone your fork locally.
2. Make changes and submit a pull request.
3. Ensure that all new content follows the established guidelines (e.g., adding new glossary terms, improving existing explanations).
4. Review and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

By participating in AVB Academy, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

### Translation contributions
At this point the AVB Academy is available in English and German. For a German translation contribution, please see the [English–German Translation Guidelines](Translation-Guidelines-German.md).

### Creating and Converting draw.io Figures

The preferred format for explanatory figures is draw.io. Based on the draw.io source file, the corresponding SVG file will be generated with translations applied automatically.  

To ensure correct translation of technical terms, enclose each term to be translated between two `@` symbols.  

**Example:** `@@Bandwidth@@` will be translated as `Bandwidth` in the English SVG and `Bandbreite` in the German SVG.  

**Important:** All translatable terms must be defined in `data/termbase.yaml`.

To generate all SVGs from the draw.io files, run:  
```bash
./build.sh --images
```

## Disclaimer

AVB Academy is a personal statement and is not affiliated with Avnu or any other organizations involved in Milan standardization. The content presented on this website is for educational purposes and does not represent official positions or standards.

## Contact and Support

For any questions or feedback, please reach out to:

- Email: info #at# avb-academy.com
- GitHub Issues: https://github.com/avb-academy/avb_academy/issues

## Acknowledgments

Special thanks to the contributors and the open-source tools that helped build AVB Academy.