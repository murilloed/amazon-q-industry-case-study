package org.example.research;

public class InvoiceService {
    public String classify(InvoiceRequest request) {
        if (request == null) {
            throw new IllegalArgumentException("request is required");
        }
        return request.getItemCount() >= 10 ? "BULK" : "STANDARD";
    }
}
