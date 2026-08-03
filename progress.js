const levels = ['🤨', '🧐', '🙂', '😌', '😎'];

for (const button of document.querySelectorAll('.progress')) {
	const key = 'progress:' + button.dataset.key;

	const saved = localStorage.getItem(key);
	if (saved)
		button.textContent = saved;

	button.addEventListener('click', () => {
		const next = levels[(levels.indexOf(button.textContent) + 1) % levels.length];
		button.textContent = next;
		localStorage.setItem(key, next);
	});
}
