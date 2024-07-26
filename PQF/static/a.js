function copyToClipboard() {
    var formattedQuery = document.querySelector('pre code');
    var range = document.createRange();
    range.selectNode(formattedQuery);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand('copy');
    alert('Copied to clipboard!');
}
