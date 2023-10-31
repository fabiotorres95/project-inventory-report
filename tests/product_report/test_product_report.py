from inventory_report.product import Product


def test_product_report() -> None:
    good_report = Product(
        "1",
        "Banana",
        "Banana Republic",
        "01-01-2021",
        "02-02-2022",
        "987654321",
        "Eat it before it rots",
    )

    assert str(good_report) == (
        "The product 1 - Banana "
        "with serial number 987654321 "
        "manufactured on 01-01-2021 "
        "by the company Banana Republic "
        "valid until 02-02-2022 "
        "must be stored according to the following instructions: "
        "Eat it before it rots."
    )
