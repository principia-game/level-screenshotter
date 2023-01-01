
def main():
	text = ""
	with open("/home/rollerozxa/.principia/settings.ini", 'r') as f:
		text = f.read()

	if 'render_gui=1' in text:
		print("disabling gui")
		text = text.replace('render_gui=1', 'render_gui=0')
		text = text.replace('display_fps=1', 'display_fps=0')

	else:
		print("enabling gui")
		text = text.replace('render_gui=0', 'render_gui=1')
		text = text.replace('display_fps=0', 'display_fps=1')

	with open("/home/rollerozxa/.principia/settings.ini", 'w') as f:
		f.write(text)

if __name__ == "__main__":
	main()
