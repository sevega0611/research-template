Guide the user through setting up the project on a new machine.

Steps:
1. Ask the user: "What operating system are you on? (Mac / Windows)"
2. Walk them through each step from `docs/setup.md`, tailored to their OS.
3. After each step, ask: "Done? Any errors?" before continuing.
4. Key steps to cover:
   - Install Git
   - Configure Git identity
   - Install GitHub CLI and authenticate
   - Install Python
   - Clone the repository
   - Install Python dependencies (`pip install -r requirements.txt`)
   - Add their username and paths to `config.py`
   - Create `.env` from `.env.example` and add API keys
   - Verify Dropbox folder access
   - Test setup with `python config.py`
5. If they hit an error, help them debug it before continuing.
6. End with: "Setup complete. Run `/status` to see the current state of the project."
