import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"❌ Error ejecutando: {' '.join(command)}")
        sys.exit(1)

def main():
    print("🔧 Ejecutando git add .")
    run_command(["git", "add", "."])

    commit_message = input("📝 Commit message: ").strip()

    if not commit_message:
        print("❌ El mensaje de commit no puede estar vacío")
        sys.exit(1)

    print(f"🔧 Ejecutando git commit -m \"{commit_message}\"")
    run_command(["git", "commit", "-m", commit_message])

    print("🚀 Ejecutando git push")
    run_command(["git", "push"])

    print("✅ Push completado con éxito")

if __name__ == "__main__":
    main()