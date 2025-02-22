import requests
from pydantic import BaseModel, RootModel


class Unit(BaseModel):
    price: float
    per: str


class Price(BaseModel):
    current: float
    lpp: bool
    unit: Unit
    type: str


class Image(BaseModel):
    url: str
    alt_text: str | None = None


class Product(BaseModel):
    sku: str
    name: str
    description: str | None = None
    price: Price | None = None
    images: list[Image] = []
    availability: str | None = None
    catchWeight: str | None = None


class ProductsBySku(RootModel[dict[str, Product]]):
    pass


class Products(BaseModel):
    productsBySku: ProductsBySku


class ChildCategory(BaseModel):
    id: str
    name: str
    lastModified: str
    children: list["ChildCategory"] | None = None  # Recursive structure


class Catalogue(BaseModel):
    childCategories: dict[str, ChildCategory]
    error: str | None = None


class Breadcrumbs(BaseModel):
    catalogue: Catalogue


class BrowserWarnings(BaseModel):
    isUnsupportedBrowserAlertOpen: bool
    isOfflineAlertOpen: bool
    isOffline: bool


class CookieDisclaimer(BaseModel):
    userHidDisclaimer: bool


class Coupons(BaseModel):
    isInfoSectionCollapsed: bool


class FeedbackOption(BaseModel):
    value: str
    name: str


class FeedbackPopup(BaseModel):
    feedbackOptions: list[FeedbackOption]
    hasError: bool
    isPopupOpened: bool
    isFeedbackSent: bool


class SectionLink(BaseModel):
    url: str
    title: str


class Link(BaseModel):
    url: str
    title: str


class FooterSectionLink(BaseModel):
    sectionLink: SectionLink
    links: list[Link]


class SocialLink(BaseModel):
    id: str
    title: str
    url: str


class AppLink(BaseModel):
    id: str
    title: str
    url: str


class Footer(BaseModel):
    sectionLinks: list[FooterSectionLink]
    socialLinks: list[SocialLink]
    appLinks: list[AppLink]
    mhraLogo: str | None
    cookieLink: str | None
    error: str | None
    pageReloading: bool


class CancelOrderChangesWarning(BaseModel):
    warningVisible: bool


class MiniTrolley(BaseModel):
    position: int


class MultiSearch(BaseModel):
    isEditable: bool
    searchTerms: list[str]
    error: str | None


class PostcodeBanner(BaseModel):
    isFetching: bool
    isReceived: bool
    isHidden: bool


class LastSearch(BaseModel):
    term: str
    searchId: str


class Search(BaseModel):
    value: str
    searchSuggestions: dict[str, str]
    lastSearch: LastSearch


class Header(BaseModel):
    cancelOrderChangesWarning: CancelOrderChangesWarning
    miniTrolley: MiniTrolley
    multiSearch: MultiSearch
    postcodeBanner: PostcodeBanner
    search: Search


class InitialState(BaseModel):
    breadcrumbs: Breadcrumbs
    browserWarnings: BrowserWarnings
    cookieDisclaimer: CookieDisclaimer
    coupons: Coupons
    feedbackPopup: FeedbackPopup
    footer: Footer
    header: Header
    products: Products | None = None
