<?php
include "db_con.php";

$sql_intents = "SELECT `intent_id`, `intent_name`, `status_file` FROM `intents`";
$result = $conn->query($sql_intents);

if ($result && $result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $intent_id = $row['intent_id'];
        $intent_name = $row['intent_name'];
        $status_file = $row['status_file'];
        ?>
        <div class="card">
            <a href="intent_details.php?intent_id=<?php echo $intent_id; ?>" class="card-link">
                <div class="card-body">
                    <h5 class="card-title"><?php echo $intent_name; ?></h5>
                    <?php if ($status_file == 1) { ?>
                        <p class="text-success">Đã ghi file</p>
                    <?php } else { ?>
                        <p class="text-danger">Chưa ghi file</p>
                    <?php } ?>
                    <input type="submit" name="" hidden value="<?php echo $intent_id ?>">
                </div>
            </a>
            <?php if ($status_file == 0) { ?> <!-- Kiểm tra status_file -->
                <form method="post" action="delete_intent.php" onsubmit="return confirmDelete();">
                    <input type="hidden" name="intent_id" value="<?php echo $intent_id ?>">
                    <input type="submit" class="btn btn-danger" value="Xoa" name="delete_intent">
                </form>
            <?php } ?>
        </div>

        <script>
            function confirmDelete() {
                return confirm("Bạn có chắc chắn muốn xóa?");
            }
        </script>

        <?php
    }
} else {
    echo "Không có chủ đề nào được tìm thấy.";
}
?>
