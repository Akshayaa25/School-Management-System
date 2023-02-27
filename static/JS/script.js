function delData()
{
    text='Are you sure you want to delete?'
    if (confirm(text)==true)
    {
        del = document.getElementById('delete');
        del.href="deleteData/{{data.id}}";
    }
}

function confirmDelete(id) {
    if (confirm("Are you sure you want to delete this data?")) {
        window.location.href = "deleteData/" + id + "/";
    }
}

