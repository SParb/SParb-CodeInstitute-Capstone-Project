const editPostButton = document.getElementById("postEdit");

const deletePostButton = document.getElementById("postDelete");
const deletePostModal = new bootstrap.Modal(document.getElementById("deletePostModal"));
const confirmDeletePost = document.getElementById("confirmDeletePost");

if (editPostButton) {
    editPostButton.addEventListener("click", function() {
        const postId = editPostButton.getAttribute("post_id");
        window.location.href = `/${postId}/edit-post/`;
    });
}

if (deletePostButton) {
    deletePostButton.addEventListener("click", function() {
        const postId = deletePostButton.getAttribute("post_id");
        confirmDeletePost.href = `/${postId}/delete-post/`;
        deletePostModal.show();
    });
}


