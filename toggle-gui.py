from pathlib import Path

def main():
	text = ""
	with open("/home/administrator/.principia/settings.ini", 'r') as f:
		text = f.read()

	if 'render_gui=1' in text:
		print("disabling gui")
		text = text.replace('render_gui=1', 'render_gui=0')
		text = text.replace('display_fps=1', 'display_fps=0')

		# hackily disable reshade
		reshade_dll = Path("/usr/share/principia/opengl32.dll")
		if reshade_dll.exists():
			reshade_dll.rename(reshade_dll.with_suffix('.bak'))

	else:
		print("enabling gui")
		text = text.replace('render_gui=0', 'render_gui=1')
		text = text.replace('display_fps=0', 'display_fps=1')

		# reenable the hackily disabled reshade
		reshade_dll = Path("/usr/share/principia/opengl32.bak")
		if reshade_dll.exists():
			reshade_dll.rename(reshade_dll.with_suffix('.dll'))

	with open("/home/administrator/.principia/settings.ini", 'w') as f:
		f.write(text)

if __name__ == "__main__":
	main()
