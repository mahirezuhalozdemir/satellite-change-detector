document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("createMaskBtn").addEventListener("click", function(e) {
        e.preventDefault();
        document.getElementById("fileInput").click();
    });

    document.getElementById("fileInput").addEventListener("change", function() {
        if (this.files.length > 0) {
            console.log("Seçilen dosya:", this.files[0].name);
            // Burada yükleme veya başka işlem başlatabilirsiniz
        }s
    });
});
