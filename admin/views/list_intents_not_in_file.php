<?php
include "../../includes/db_con.php";

$sql_intents = "SELECT DISTINCT i.intent_name,i.intent_id, i.selected
FROM `intents` i 
JOIN example_intent e ON e.intent_id = i.intent_id 
JOIN answer_intent a ON a.intent_id = i.intent_id 
WHERE e.status_file = '0' OR a.status_file = '0'";
$result = $conn->query($sql_intents);

if ($result && $result->num_rows > 0) {
    ?>
    <!-- Bao gồm phiên bản đầy đủ của jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        function updateSelected(intent_id, selected) {
            $.ajax({
                url: 'update_selected.php',
                type: 'POST',
                data: {
                    intent_id: intent_id,
                    selected: selected
                },
                success: function(response) {
                    console.log('Cập nhật thành công');
                },
                error: function() {
                    console.log('Cập nhật thất bại');
                }
            });
        }

        $(document).ready(function() {
            $('input[type="checkbox"]').change(function() {
                var intent_id = $(this).val();
                var selected = $(this).is(':checked') ? 1 : 0;
                updateSelected(intent_id, selected);
            });
        });
    </script>
    <?php
    while ($row = $result->fetch_assoc()) {
        $intent_id = $row['intent_id'];
        $intent_name = $row['intent_name'];
        $selected = $row['selected'];
        ?>
        <div class="card" style="position: relative; padding-top: 30px;">
            <a href="./intent_detail.php?intent_id=<?php echo $intent_id; ?>" class="card-link">
                <div class="card-body">
                    <h5 class="card-title"><?php echo $intent_name; ?></h5>
                </div>
            </a>
            <div class="checkbox-container" style="position: absolute; top: 10px; right: 10px;">
            Chọn để ghi file
                <input type="checkbox" name="select_intent" value="<?php echo $intent_id; ?>" <?php echo $selected ? 'checked' : ''; ?>>
            </div>
            <form method="post" action="delete_intent.php" onsubmit="return confirmDelete();">
                <input type="hidden" name="intent_id" value="<?php echo $intent_id; ?>">
                <input type="submit" class="btn btn-danger" value="Xóa" name="delete_intent">
            </form>
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
