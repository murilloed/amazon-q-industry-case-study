package org.example.research;

public class InvoiceRequest {
    private final String customerReference;
    private final int itemCount;

    public InvoiceRequest(String customerReference, int itemCount) {
        this.customerReference = customerReference;
        this.itemCount = itemCount;
    }

    public String getCustomerReference() {
        return customerReference;
    }

    public int getItemCount() {
        return itemCount;
    }
}
