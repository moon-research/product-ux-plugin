#!/bin/bash
set -e

# Lean setup for a UX designer working with Claude Code + Codex.
# Derived from setup.sh with databases, Kubernetes, Docker, extra language
# toolchains and Powerlevel10k left out.

echo "=== Mac Setup (UX Designer) ==="
echo ""

# Check if Homebrew is installed
if ! command -v brew &>/dev/null; then
  echo "Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  # Make brew available in this session (Apple Silicon / Intel)
  if [ -x /opt/homebrew/bin/brew ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
  elif [ -x /usr/local/bin/brew ]; then
    eval "$(/usr/local/bin/brew shellenv)"
  fi
else
  echo "Homebrew already installed, updating..."
  brew update
fi

echo ""
echo "=== CLI Tools ==="
# git/gh: version control and GitHub login
# node + pnpm: React/JS toolchain, also needed to install the Claude Code and Codex CLIs
# python + uv: many agent skills and scripts run Python
# jq, ripgrep, tree: used by the agents when exploring projects
brew install git git-lfs gh node pnpm python uv jq ripgrep tree tmux cloudflare-wrangler

echo ""
echo "=== AI Coding Agents ==="
npm install -g @anthropic-ai/claude-code @openai/codex typescript

echo ""
echo "=== Oh My Zsh + Plugins ==="
if [ ! -d "$HOME/.oh-my-zsh" ]; then
  echo "Installing Oh My Zsh..."
  RUNZSH=no KEEP_ZSHRC=yes sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
else
  echo "Oh My Zsh already installed, skipping."
fi
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions 2>/dev/null || echo "zsh-autosuggestions already installed"
git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting 2>/dev/null || echo "zsh-syntax-highlighting already installed"

echo ""
echo "=== Fonts ==="
brew install --cask font-inter font-jetbrains-mono

echo ""
echo "=== Applications ==="
brew install --cask google-chrome
brew install --cask figma
brew install --cask visual-studio-code
brew install --cask claude
brew install --cask chatgpt

echo ""
echo "=== VS Code Extensions (React) ==="
for ext in dbaeumer.vscode-eslint esbenp.prettier-vscode bradlc.vscode-tailwindcss dsznajder.es7-react-js-snippets formulahendry.auto-rename-tag; do
  code --install-extension "$ext" --force || echo "Could not install $ext, skipping."
done

echo ""
echo "=== Git Config ==="
read -p "Git user name: " git_name
read -p "Git email: " git_email
git config --global user.name "$git_name"
git config --global user.email "$git_email"
git config --global init.defaultBranch main
git config --global pull.rebase true
git config --global push.autoSetupRemote true
git lfs install

echo ""
echo "=== SSH Key ==="
if [ ! -f ~/.ssh/id_ed25519 ]; then
  ssh-keygen -t ed25519 -C "$git_email"
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_ed25519
  echo ""
  echo "Your public key (add to GitHub):"
  cat ~/.ssh/id_ed25519.pub
else
  echo "SSH key already exists, skipping."
fi

echo ""
echo "=== Shell Config ==="
ZSHRC=~/.zshrc

# Back up existing .zshrc
[[ -f "$ZSHRC" ]] && cp "$ZSHRC" "$ZSHRC.bak"

cat > "$ZSHRC" << 'SHELL_CONFIG'
# Homebrew
if [[ -x /opt/homebrew/bin/brew ]]; then
  eval "$(/opt/homebrew/bin/brew shellenv)"
elif [[ -x /usr/local/bin/brew ]]; then
  eval "$(/usr/local/bin/brew shellenv)"
fi

# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="robbyrussell"

plugins=(git copypath copyfile dirhistory macos node npm gh sudo history-substring-search zsh-autosuggestions zsh-syntax-highlighting)

setopt HIST_IGNORE_DUPS # no duplicate history entries
setopt SHARE_HISTORY    # share history across terminals

source $ZSH/oh-my-zsh.sh

# Python - use python3 / pip3 by default
alias python=python3
alias pip=pip3

# Claude Code
export PATH="$HOME/.local/bin:$PATH"
SHELL_CONFIG

echo ""
echo "=== Done! ==="
echo "Restart your terminal or run: source ~/.zshrc"
echo ""
echo "Next steps:"
echo "  gh auth login          # authenticate with GitHub"
echo "  wrangler login         # authenticate with Cloudflare"
echo "  claude                 # start Claude Code and sign in"
echo "  codex                  # start Codex and sign in"
