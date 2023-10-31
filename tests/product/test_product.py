from inventory_report.product import Product


def test_create_product() -> None:
    good_product = Product(
        "123",
        "product_name",
        "company_name",
        "manufacturing_date",
        "expiration_date",
        "serial_number",
        "storage_instructions",
    )

    assert good_product.id == "123"
    assert good_product.product_name == "product_name"
    assert good_product.company_name == "company_name"
    assert good_product.manufacturing_date == "manufacturing_date"
    assert good_product.expiration_date == "expiration_date"
    assert good_product.serial_number == "serial_number"
    assert good_product.storage_instructions == "storage_instructions"
