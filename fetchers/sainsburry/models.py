from pydantic import BaseModel


class UnitPrice(BaseModel):
    price: float
    measure: str
    measure_amount: int


class RetailPrice(BaseModel):
    price: float
    measure: str


class Label(BaseModel):
    label_uid: str
    text: str
    alt_text: str
    color: str
    link_opens_in_new_window: bool


class Review(BaseModel):
    is_enabled: bool
    product_uid: str
    total: int
    average_rating: float


class Asset(BaseModel):
    plp_image: str
    images: list[str]
    video: list[str]


class Category(BaseModel):
    id: str
    name: str


class Promotion(BaseModel):
    promotion_uid: str
    icon: str
    link: str
    strap_line: str
    start_date: str
    end_date: str
    original_price: float
    promo_mechanic_id: str
    is_nectar: bool
    promo_type: str
    promo_group: str


class Header(BaseModel):
    text: str
    type: str


class Attribute(BaseModel):
    brand: list[str]


class Product(BaseModel):
    product_uid: str
    favourite_uid: str | None = None
    eans: list[str]
    product_type: str
    name: str
    # image: str
    # image_zoom: str | None = None
    # image_thumbnail: str
    # image_thumbnail_small: str
    full_url: str
    unit_price: UnitPrice | None = None  # Made optional
    retail_price: RetailPrice | None = None  # Made optional
    nectar_price: dict[str, float | str] | None = None
    is_available: bool
    promotions: list[Promotion]
    associations: list[str]
    is_alcoholic: bool
    is_spotlight: bool
    is_intolerant: bool
    is_mhra: bool
    badges: list[str]
    labels: list[Label]
    zone: str | None = None
    department: str | None = None
    # reviews: Review
    breadcrumbs: list[str]
    assets: Asset
    # description: list[str]
    # important_information: list[str]
    attachments: list[str]
    categories: list[Category]
    header: Header | None = None  # Made optional
    attributes: Attribute | None = None
    is_supply_chain_orderable: bool | None = None
    # display_icons: list[str]
    # pdp_deep_link: str


class Value(BaseModel):
    id: str | None = None  # Made optional
    label: str
    value: str
    selected: bool
    enabled: bool


class Filter(BaseModel):
    key: str
    label: str
    type: str
    values: list[Value]


class SortOption(BaseModel):
    display: str
    value: str


class Sort(BaseModel):
    active: str
    options: list[SortOption]


class Page(BaseModel):
    active: int
    first: int
    last: int
    size: int
    size_options: list[int]


class Controls(BaseModel):
    sort: Sort
    total_record_count: int
    returned_record_count: int
    page: Page
    filters: list[Filter]


class SainsburryData(BaseModel):
    products: list[Product]
    controls: Controls

# Example usage:
# data = SainsburryData.parse_raw(json_string)
