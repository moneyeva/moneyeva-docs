document$.subscribe(function() {
    $('table').DataTable({
        paging: true,         // Enable pagination
        searching: true,      // Enable search functionality
        ordering: true,       // Enable column sorting
        pageLength: 50,       // Set the number of rows per page
    });
});