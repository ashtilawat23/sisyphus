import subprocess

def get_changed_files():
    # Use Git to get a list of changed files in the last merge
    # This command might need to be adjusted based on your specific needs
    result = subprocess.run(['git', 'diff', '--name-only', 'HEAD', 'HEAD~1'], capture_output=True, text=True)
    changed_files = result.stdout.splitlines()
    return changed_files

def summarize_changes(changed_files):
    # Simple summary of changes
    summary = f"Changed files: {len(changed_files)}\n"
    summary += "\n".join(changed_files)
    return summary

def main():
    changed_files = get_changed_files()
    summary = summarize_changes(changed_files)
    print(summary)

    # Optionally, write the summary to a file or pass it to another script
    with open('code_change_summary.txt', 'w') as file:
        file.write(summary)

if __name__ == "__main__":
    main()