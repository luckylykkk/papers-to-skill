#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

const packageRoot = path.resolve(__dirname, "..");
const skillSource = path.join(packageRoot, "skills", "papers-to-skill");
const pluginSource = packageRoot;
const marketplaceSource = path.join(packageRoot, "marketplace");

function usage() {
  console.log(`papers-to-skill

Usage:
  papers-to-skill paths
  papers-to-skill install <codex|hermes|openclaw|skill-dir> [--dest <path>] [--force]
  papers-to-skill plugin-path
  papers-to-skill skill-path

Examples:
  papers-to-skill install codex
  papers-to-skill install hermes
  papers-to-skill install openclaw --dest /path/to/openclaw/skills/papers-to-skill
  papers-to-skill install skill-dir --dest /path/to/agent/skills/papers-to-skill
`);
}

function parseOptions(argv) {
  const opts = { _: [] };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--force") {
      opts.force = true;
    } else if (arg === "--dest") {
      i += 1;
      if (!argv[i]) throw new Error("--dest requires a path");
      opts.dest = argv[i];
    } else if (arg === "-h" || arg === "--help") {
      opts.help = true;
    } else {
      opts._.push(arg);
    }
  }
  return opts;
}

function defaultDest(target) {
  const home = os.homedir();
  if (target === "codex") {
    return path.join(home, ".codex", "skills", "papers-to-skill");
  }
  if (target === "hermes") {
    return path.join(home, ".hermes", "skills", "research", "papers-to-skill");
  }
  if (target === "openclaw") {
    const skillsDir = process.env.OPENCLAW_SKILLS_DIR;
    if (skillsDir) return path.join(skillsDir, "papers-to-skill");
    return path.join(home, ".openclaw", "skills", "papers-to-skill");
  }
  return null;
}

function copySkill(dest, force) {
  if (!fs.existsSync(skillSource)) {
    throw new Error(`Skill source not found: ${skillSource}`);
  }
  if (fs.existsSync(dest)) {
    if (!force) {
      throw new Error(`Destination already exists: ${dest}\nUse --force to replace it.`);
    }
    fs.rmSync(dest, { recursive: true, force: true });
  }
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.cpSync(skillSource, dest, { recursive: true });
  console.log(`Installed papers-to-skill skill to:\n${dest}`);
}

function printPaths() {
  console.log(JSON.stringify({
    packageRoot,
    pluginSource,
    marketplaceSource,
    skillSource,
    claudeCodePluginValidate: `claude plugin validate "${pluginSource}"`,
    claudeCodeMarketplaceAdd: `claude plugin marketplace add "${marketplaceSource}"`,
    claudeCodeMarketplaceInstall: "claude plugin install papers-to-skill@papers-to-skill-marketplace"
  }, null, 2));
}

async function main() {
  const opts = parseOptions(process.argv.slice(2));
  const [cmd, target] = opts._;

  if (!cmd || opts.help) {
    usage();
    return;
  }

  if (cmd === "paths") {
    printPaths();
    return;
  }

  if (cmd === "plugin-path") {
    console.log(pluginSource);
    return;
  }

  if (cmd === "skill-path") {
    console.log(skillSource);
    return;
  }

  if (cmd === "install") {
    if (!target) throw new Error("install requires a target");
    if (target === "claude-code") {
      console.log(`Claude Code plugin root:\n${pluginSource}\n`);
      console.log(`Validate:\nclaude plugin validate "${pluginSource}"\n`);
      console.log(`Local marketplace install:\nclaude plugin marketplace add "${marketplaceSource}"\nclaude plugin install papers-to-skill@papers-to-skill-marketplace`);
      return;
    }
    const dest = opts.dest || defaultDest(target);
    if (!dest) {
      throw new Error(`Unknown target: ${target}`);
    }
    copySkill(path.resolve(dest), Boolean(opts.force));
    return;
  }

  throw new Error(`Unknown command: ${cmd}`);
}

main().catch((error) => {
  console.error(`papers-to-skill: ${error.message}`);
  process.exit(1);
});
