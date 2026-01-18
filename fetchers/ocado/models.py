"""Pydantic models for Ocado responses."""

from pydantic import BaseModel, RootModel


class Unit(BaseModel):
    """Unit price details."""

    price: float
    per: str


class Price(BaseModel):
    """Price information for a product."""

    current: float
    lpp: bool
    unit: Unit
    type: str


class Image(BaseModel):
    """Image metadata for a product."""

    url: str
    alt_text: str | None = None


class Product(BaseModel):
    """Product metadata from Ocado."""

    sku: str
    name: str
    description: str | None = None
    price: Price | None = None
    images: list[Image] = []
    availability: str | None = None
    catchWeight: str | None = None


class ProductsBySku(RootModel[dict[str, Product]]):
    """Products indexed by SKU."""

    pass


class Products(BaseModel):
    """Container for product mappings."""

    productsBySku: ProductsBySku


class ChildCategory(BaseModel):
    """Catalog category entry."""

    id: str
    name: str
    lastModified: str
    children: list["ChildCategory"] | None = None  # Recursive structure


class Catalogue(BaseModel):
    """Catalog details."""

    childCategories: dict[str, ChildCategory]
    error: str | None = None


class Breadcrumbs(BaseModel):
    """Breadcrumb metadata."""

    catalogue: Catalogue


class BrowserWarnings(BaseModel):
    """Browser warning status flags."""

    isUnsupportedBrowserAlertOpen: bool
    isOfflineAlertOpen: bool
    isOffline: bool


class CookieDisclaimer(BaseModel):
    """Cookie disclaimer state."""

    userHidDisclaimer: bool


class Coupons(BaseModel):
    """Coupons UI state."""

    isInfoSectionCollapsed: bool


class FeedbackOption(BaseModel):
    """Feedback option details."""

    value: str
    name: str


class FeedbackPopup(BaseModel):
    """Feedback popup state."""

    feedbackOptions: list[FeedbackOption]
    hasError: bool
    isPopupOpened: bool
    isFeedbackSent: bool


class SectionLink(BaseModel):
    """Footer section link."""

    url: str
    title: str


class Link(BaseModel):
    """Generic link entry."""

    url: str
    title: str


class FooterSectionLink(BaseModel):
    """Footer section with nested links."""

    sectionLink: SectionLink
    links: list[Link]


class SocialLink(BaseModel):
    """Social link entry."""

    id: str
    title: str
    url: str


class AppLink(BaseModel):
    """App download link entry."""

    id: str
    title: str
    url: str


class Footer(BaseModel):
    """Footer content and metadata."""

    sectionLinks: list[FooterSectionLink]
    socialLinks: list[SocialLink]
    appLinks: list[AppLink]
    mhraLogo: str | None
    cookieLink: str | None
    error: str | None
    pageReloading: bool


class CancelOrderChangesWarning(BaseModel):
    """Order change warning state."""

    warningVisible: bool


class MiniTrolley(BaseModel):
    """Mini trolley UI state."""

    position: int


class MultiSearch(BaseModel):
    """Multi-search UI state."""

    isEditable: bool
    searchTerms: list[str]
    error: str | None


class PostcodeBanner(BaseModel):
    """Postcode banner state."""

    isFetching: bool
    isReceived: bool
    isHidden: bool


class LastSearch(BaseModel):
    """Last search metadata."""

    term: str
    searchId: str


class Search(BaseModel):
    """Search header metadata."""

    value: str
    searchSuggestions: dict[str, str]
    lastSearch: LastSearch


class Header(BaseModel):
    """Header UI state."""

    cancelOrderChangesWarning: CancelOrderChangesWarning
    miniTrolley: MiniTrolley
    multiSearch: MultiSearch
    postcodeBanner: PostcodeBanner
    search: Search


class InitialState(BaseModel):
    """Top-level initial state payload."""

    breadcrumbs: Breadcrumbs
    browserWarnings: BrowserWarnings
    cookieDisclaimer: CookieDisclaimer
    coupons: Coupons
    feedbackPopup: FeedbackPopup
    footer: Footer
    header: Header
    products: Products | None = None
