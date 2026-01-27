from fastapi import APIRouter, HTTPException
from ucp_sdk.models.schemas.shopping.checkout_create_req import CheckoutCreateRequest
from ucp_sdk.models.schemas.shopping.checkout_resp import CheckoutResponse, ResponseCheckout
from ucp_sdk.models.schemas.shopping.payment_create_req import PaymentCreateRequest
from ucp_sdk.models.schemas.shopping.payment_resp import PaymentResponse
from ucp_sdk.models.schemas.shopping.fulfillment_create_req import FulfillmentExtensionCreateRequest
from ucp_sdk.models.schemas.shopping.fulfillment_resp import FulfillmentExtensionResponse
from ucp_sdk.models.schemas.shopping.types.line_item_resp import LineItemResponse
from ucp_sdk.models.schemas.shopping.types.total_resp import TotalResponse
from ucp_sdk.models.schemas.shopping.types.link import Link
from ucp_sdk.models.schemas.shopping.types.item_resp import ItemResponse

router = APIRouter()

@router.post("/checkout", response_model=CheckoutResponse)
async def create_checkout(checkout_req: CheckoutCreateRequest):
    """
    Create a new checkout session.
    """
    # Mock implementation
    # In a real implementation, this would save to a database

    # Constructing a valid mock response
    response_ucp = ResponseCheckout(
        version="2024-01-01",
        capabilities=[
            {"name": "ucp.shopping", "version": "2024-01-01"}
        ]
    )

    mock_line_items = [
        LineItemResponse(
            id="item_1",
            quantity=1,
            item=ItemResponse(
                id="product_1",
                title="AI Generated Widget",
                price=1000,
                image_url="https://example.com/widget.jpg"
            ),
            totals=[
                TotalResponse(type="subtotal", amount=1000),
                TotalResponse(type="total", amount=1000)
            ]
        )
    ]

    mock_totals = [
        TotalResponse(type="subtotal", amount=1000),
        TotalResponse(type="tax", amount=100),
        TotalResponse(type="total", amount=1100)
    ]

    mock_links = [
        Link(type="self", url="https://api.example.com/ucp/checkout/123"),
        Link(type="payment", url="https://api.example.com/ucp/payment")
    ]

    mock_payment = PaymentResponse(
        handlers=[]
    )

    return CheckoutResponse(
        ucp=response_ucp,
        id="checkout_123",
        line_items=mock_line_items,
        status="incomplete",
        currency="USD",
        totals=mock_totals,
        links=mock_links,
        payment=mock_payment
    )

@router.post("/payment", response_model=PaymentResponse)
async def create_payment(payment_req: PaymentCreateRequest):
    """
    Handle payment creation/update.
    """
    # Mock implementation
    return PaymentResponse(
        handlers=[]
    )

@router.post("/fulfillment", response_model=FulfillmentExtensionResponse)
async def create_fulfillment(fulfillment_req: FulfillmentExtensionCreateRequest):
    """
    Handle fulfillment options.
    """
    # Mock implementation - returning empty/null for the root model as it is defined as Any
    return FulfillmentExtensionResponse(root=None)
