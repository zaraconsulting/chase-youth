$('#snapchat').on('mouseover', () => {
    $('#snapchat-copy-link').text('Click to copy');
});
$('#snapchat').on('mouseout', () => {
    $('#snapchat-copy-link').text('$CHASEYOUTH');
});

function copyToClipboard()
{
    const el = document.createElement('textarea');
    el.value = '$CHASEYOUTH';
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);

    $('#snapchat-copy-link').text('Copied!');
    setTimeout(() =>
    {
        $('#snapchat-copy-link').text('$CHASEYOUTH');
    }, 2000);


}
// document.querySelector('#snapchat-copy-link').addEventListener('click', copyToClipboard)