
██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ██╗███████╗████████╗███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     ██║███████╗   ██║   █████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██║╚════██║   ██║   ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║███████║   ██║   ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                      
```WordlistForge is an advanced wordlist generator specifically designed for creating targeted wordlists for various social media platforms and online services. It uses platform-specific patterns and user information to generate potential passwords.```
🚨 Disclaimer
This tool is for educational and ethical security testing purposes only.

Only use this tool on accounts you own or have explicit permission to test
Unauthorized access to computer systems is illegal and unethical
The author is not responsible for misuse of this software

## ✨ Key Features

- **Platform Intelligence**: Implements unique password creation patterns for 15+ major social platforms
- **Advanced Pattern Recognition**: Analyzes how users typically create passwords on specific platforms
- **Dynamic Wordlist Generation**: Creates customized wordlists based on personal information and platform habits
- **Comprehensive Complexity Options**:
  - Leetspeak transformations (a→4, e→3, etc.)
  - Special character insertions
  - Case modifications
  - Number appendages
  - Year variations
  - Complex combinations
- **User-Friendly Interface**:
  - Terminal-based colorful UI
  - Interactive prompts
  - Real-time progress indicators
  - Typing effects and spinners
- **Performance Optimization**:
  - Smart filtering algorithms
  - Duplicate prevention
  - Wordlist size control
  - Priority-based password generation
- **Security-Focused**:
  - Local processing (no data leaves your system)
  - No internet connectivity required
  - Secure file handling

## 🌐 Supported Platforms

| Social Platforms | Gaming Platforms | Professional Platforms |
|------------------|------------------|------------------------|
| Instagram        | Steam            | LinkedIn               |
| Facebook         | PlayStation      | GitHub                 |
| Twitter/X        | Xbox/Microsoft   | Custom/Other           |
| TikTok           | Twitch           |                        |
| Snapchat         | Discord          |                        |
| Pinterest        |                  |                        |
| YouTube          |                  |                        |
| Reddit           |                  |                        |

## 🔧 Installation

### System Requirements

- Python 3.6 or higher
- 512MB+ RAM
- 10MB disk space (plus space for generated wordlists)
- Linux, macOS, or Windows with terminal access

### Dependencies

WordlistForge has no external dependencies beyond Python's standard library, making it easy to deploy anywhere Python runs.

### Installation on Linux

#### Method 1: Standard Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/wordlistforge.git

# Navigate to the directory
cd wordlistforge

# Make the script executable
chmod +x wordlistforge.py

# Run the tool
./wordlistforge.py
```

## 🚀 Usage Guide

### Basic Usage

1. Start the tool:
   ```bash
   ./wordlistforge.py
   ```

2. Follow the interactive prompts:
   - Select the target platform
   - Enter known information about the target (with proper authorization)
   - Configure complexity options
   - Select wordlist size preference

3. The tool will generate a customized wordlist saved to the `wordlists/` directory.

### Advanced Usage

#### Wordlist Sizes

- **Small**: ~1,000 passwords (highly targeted, best for quick tests)
- **Medium**: ~5,000 passwords (balanced approach, recommended)
- **Large**: ~10,000 passwords (comprehensive, best for thorough testing)

#### Platform-Specific Strategies

For optimal results, consider platform-specific patterns:

- **Instagram**: Focus on photography-related terms, handles with underscores
- **Twitter/X**: Short usernames with numbers, concise combinations
- **Gaming Platforms**: Often include gaming terms, leetspeak, and numbers
- **Professional Platforms**: Usually more formal, less leetspeak, more full names

### Real-world Example Session

```
██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ██╗███████╗████████╗███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     ██║███████╗   ██║   █████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██║╚════██║   ██║   ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║███████║   ██║   ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                      ENHANCED EDITION

[+] Available Platforms:
  [1] Instagram
  [2] Facebook
  [3] Twitter/X
  [4] TikTok
  [5] Snapchat
  [...]

[?] Select target platform: 1

[+] Collecting information for Instagram wordlist generation...
Target username: photosmith
First name: John
Last name: Smith
Pet name (if any): Rex
Date of birth (DD/MM/YYYY): 15/08/1990
[...]

[+] Enter important locations (city, country, etc. - one per line, leave empty to finish):
  > newyork
  > chicago

[+] Enter additional words (one per line, leave empty to finish):
  > photography
  > nature
  > travel

[+] Password Complexity Options:
  [1] Include numbers (0-9)
  [2] Include special characters (!@#$%^&*)
  [3] Include uppercase letters
  [4] Include common leetspeak substitutions (a→4, e→3, etc.)
  [5] Include year variations (2020-2025)
  [6] Include extra-complex combinations

[?] Select options (comma-separated, e.g., 1,3,5): 1,3,4,5

[+] Wordlist Size Preference:
  [1] Small (fewer, more targeted passwords)
  [2] Medium (balanced approach)
  [3] Large (comprehensive, but may include unlikely passwords)

[?] Select an option: 2

[+] Generating wordlist...
[■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%

[+] Wordlist generation complete!
[+] Generated 4,853 unique passwords for Instagram
[+] Saved to: wordlists/instagram_20250225_123456.txt
```

## 📈 Using Generated Wordlists

Once your wordlist is generated, you can use it with popular security testing tools:

```bash
# With Hydra (SSH example)
hydra -l username -P wordlists/instagram_20250225_123456.txt ssh://target

# With Hashcat (MD5 example)
hashcat -m 0 -a 0 hash.txt wordlists/instagram_20250225_123456.txt

# With John the Ripper
john --wordlist=wordlists/instagram_20250225_123456.txt hash.txt
```

## 🛡️ Security Considerations

- **Local Processing**: All data processing occurs on your local machine
- **No Network Activity**: The tool never transmits user information
- **Safe Storage**: Generated wordlists are stored locally in the `wordlists/` directory
- **File Security**: Consider using full disk encryption if storing sensitive wordlists
- **Permissions**: Be cautious about who has access to your generated wordlists

## 🧠 Understanding How It Works

WordlistForge works by:

1. **Information Collection**: Gathering target information through interactive prompts
2. **Pattern Application**: Applying platform-specific password creation patterns
3. **Transformation**: Applying various transformations based on selected complexity options
4. **Filtering**: Removing duplicates and prioritizing likely passwords
5. **Output**: Generating a text file with the final wordlist

Each platform module contains specific rules and patterns derived from research on common password creation habits specific to that platform.

## 🦮 Guides and Best Practices

### For Ethical Hackers

- Always obtain written permission before testing
- Document your methodology thoroughly
- Report any vulnerabilities through proper channels
- Never share passwords or personal information discovered
- Use the minimum wordlist size necessary for your testing

### For System Administrators

- Use this tool to audit password policies
- Test password recovery mechanisms
- Identify weak passwords in your organization
- Create security awareness training based on findings
- Implement stricter password policies where necessary

## 🔄 Common Workflows

1. **Basic Security Audit**:
   ```
   Generate small wordlist → Test with minimal info → Expand if needed
   ```

2. **Comprehensive Testing**:
   ```
   Generate medium wordlist → Test common accounts → Document findings
   ```

3. **Educational Demonstration**:
   ```
   Generate wordlist for fictional persona → Show password weaknesses → Discuss improvements
   ```

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how you can contribute:

1. **Fork** the repository
2. **Create** your feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes:
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push** to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open** a Pull Request

### Development Environment Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/wordlistforge.git

# Create a virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development requirements
pip install -r dev-requirements.txt  # If available
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Original Author

- Sambhav Mehra
- Instagram: @sambhav__7__

## 🙏 Acknowledgements

- Special thanks to all ethical hackers and security researchers who contribute to safer online environments
- Thanks to the Python community for providing excellent libraries and tools
- Appreciation to all contributors who help improve this tool

## 📬 Contact

For issues, questions, or suggestions:
- Create an issue in the GitHub repository
- Contact the original author through GitHub

---

<div align="center">
  <p>Made with ❤️ for the security community</p>
  <p>Remember: With great power comes great responsibility</p>
</div>
