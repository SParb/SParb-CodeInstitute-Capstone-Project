const deletePostButton = document.getElementById("postDelete");
const deletePostModal = new bootstrap.Modal(document.getElementById("deletePostModal"));
const confirmDeletePost = document.getElementById("confirmDeletePost");

if (deletePostButton) {
    deletePostButton.addEventListener("click", function() {
        const postId = deletePostButton.getAttribute("post_id");
        confirmDeletePost.href = `/${postId}/delete_post/`;
        deletePostModal.show();
    });
}

