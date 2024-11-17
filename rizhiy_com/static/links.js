// Link management functionality
function addLinkEntry() {
    const linkEntry = document.createElement('div');
    linkEntry.className = 'link-entry';
    linkEntry.innerHTML = `
        <input type="text" name="link_urls[]" placeholder="URL" required />
        <input type="text" name="link_descs[]" placeholder="Description" />
        <button type="button" class="remove-link">Remove</button>
        <input type="hidden" name="link_ids[]" value="" />
    `;
    document.getElementById('existing-links').appendChild(linkEntry);
}

function setupLinkHandlers() {
    document.getElementById('add-link').addEventListener('click', addLinkEntry);
    document.getElementById('existing-links').addEventListener('click', function(e) {
        if (e.target.classList.contains('remove-link')) {
            e.target.closest('.link-entry').remove();
        }
    });
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', setupLinkHandlers);
