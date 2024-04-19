from __future__ import annotations

from typing import Any
from phtml5.htmlelement import HTMLElement

class Html(HTMLElement):

    def __call__(self: Html, *args: Body | Head | list[Body | Head]) -> Html:
        return Html(self._tag, self._attributes, self.get_children_from_args(args))

def html(_class: str | None = None, **kwargs: Any) -> Html:
    arguments = { 'class': _class }
    return Html('html', arguments | kwargs, [])

class Head(HTMLElement):

    def __call__(self: Head, *args: Metadatacontent | list[Metadatacontent]) -> Head:
        return Head(self._tag, self._attributes, self.get_children_from_args(args))

def head(_class: str | None = None, **kwargs: Any) -> Head:
    arguments = { 'class': _class }
    return Head('head', arguments | kwargs, [])

class Title(HTMLElement):
    pass

def title(_class: str | None = None, **kwargs: Any) -> Title:
    arguments = { 'class': _class }
    return Title('title', arguments | kwargs, [])

class Base(HTMLElement):
    pass

def base(_class: str | None = None, **kwargs: Any) -> Base:
    arguments = { 'class': _class }
    return Base('base', arguments | kwargs, [])

class Link(HTMLElement):
    pass

def link(_class: str | None = None, **kwargs: Any) -> Link:
    arguments = { 'class': _class }
    return Link('link', arguments | kwargs, [])

class Meta(HTMLElement):
    pass

def meta(_class: str | None = None, **kwargs: Any) -> Meta:
    arguments = { 'class': _class }
    return Meta('meta', arguments | kwargs, [])

class Style(HTMLElement):
    pass

def style(_class: str | None = None, **kwargs: Any) -> Style:
    arguments = { 'class': _class }
    return Style('style', arguments | kwargs, [])

class Summary(HTMLElement):

    def __call__(self: Summary, *args: Phrasingcontent | Headingcontent | str | list[Phrasingcontent | Headingcontent | str]) -> Summary:
        return Summary(self._tag, self._attributes, self.get_children_from_args(args))

def summary(_class: str | None = None, **kwargs: Any) -> Summary:
    arguments = { 'class': _class }
    return Summary('summary', arguments | kwargs, [])

class Script(HTMLElement):
    pass

def script(_class: str | None = None, **kwargs: Any) -> Script:
    arguments = { 'class': _class }
    return Script('script', arguments | kwargs, [])

class Noscript(HTMLElement):

    def __call__(self: Noscript, *args: Flowcontent | str | list[Flowcontent | str]) -> Noscript:
        return Noscript(self._tag, self._attributes, self.get_children_from_args(args))

def noscript(_class: str | None = None, **kwargs: Any) -> Noscript:
    arguments = { 'class': _class }
    return Noscript('noscript', arguments | kwargs, [])

class Body(HTMLElement):

    def __call__(self: Body, *args: Flowcontent | list[Flowcontent]) -> Body:
        return Body(self._tag, self._attributes, self.get_children_from_args(args))

def body(_class: str | None = None, **kwargs: Any) -> Body:
    arguments = { 'class': _class }
    return Body('body', arguments | kwargs, [])

class Section(HTMLElement):

    def __call__(self: Section, *args: Flowcontent | list[Flowcontent]) -> Section:
        return Section(self._tag, self._attributes, self.get_children_from_args(args))

def section(_class: str | None = None, **kwargs: Any) -> Section:
    arguments = { 'class': _class }
    return Section('section', arguments | kwargs, [])

class Nav(HTMLElement):

    def __call__(self: Nav, *args: Flowcontent | list[Flowcontent]) -> Nav:
        return Nav(self._tag, self._attributes, self.get_children_from_args(args))

def nav(_class: str | None = None, **kwargs: Any) -> Nav:
    arguments = { 'class': _class }
    return Nav('nav', arguments | kwargs, [])

class Article(HTMLElement):

    def __call__(self: Article, *args: Flowcontent | str | list[Flowcontent | str]) -> Article:
        return Article(self._tag, self._attributes, self.get_children_from_args(args))

def article(_class: str | None = None, **kwargs: Any) -> Article:
    arguments = { 'class': _class }
    return Article('article', arguments | kwargs, [])

class Aside(HTMLElement):

    def __call__(self: Aside, *args: Flowcontent | list[Flowcontent]) -> Aside:
        return Aside(self._tag, self._attributes, self.get_children_from_args(args))

def aside(_class: str | None = None, **kwargs: Any) -> Aside:
    arguments = { 'class': _class }
    return Aside('aside', arguments | kwargs, [])

class H1(HTMLElement):

    def __call__(self: H1, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> H1:
        return H1(self._tag, self._attributes, self.get_children_from_args(args))

def h1(_class: str | None = None, **kwargs: Any) -> H1:
    arguments = { 'class': _class }
    return H1('h1', arguments | kwargs, [])

class H2(HTMLElement):

    def __call__(self: H2, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> H2:
        return H2(self._tag, self._attributes, self.get_children_from_args(args))

def h2(_class: str | None = None, **kwargs: Any) -> H2:
    arguments = { 'class': _class }
    return H2('h2', arguments | kwargs, [])

class H3(HTMLElement):

    def __call__(self: H3, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> H3:
        return H3(self._tag, self._attributes, self.get_children_from_args(args))

def h3(_class: str | None = None, **kwargs: Any) -> H3:
    arguments = { 'class': _class }
    return H3('h3', arguments | kwargs, [])

class H4(HTMLElement):

    def __call__(self: H4, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> H4:
        return H4(self._tag, self._attributes, self.get_children_from_args(args))

def h4(_class: str | None = None, **kwargs: Any) -> H4:
    arguments = { 'class': _class }
    return H4('h4', arguments | kwargs, [])

class H5(HTMLElement):

    def __call__(self: H5, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> H5:
        return H5(self._tag, self._attributes, self.get_children_from_args(args))

def h5(_class: str | None = None, **kwargs: Any) -> H5:
    arguments = { 'class': _class }
    return H5('h5', arguments | kwargs, [])

class H6(HTMLElement):

    def __call__(self: H6, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> H6:
        return H6(self._tag, self._attributes, self.get_children_from_args(args))

def h6(_class: str | None = None, **kwargs: Any) -> H6:
    arguments = { 'class': _class }
    return H6('h6', arguments | kwargs, [])

class Hgroup(HTMLElement):

    def __call__(self: Hgroup, *args: H1 | H2 | H3 | H4 | H5 | H6 | list[H1 | H2 | H3 | H4 | H5 | H6]) -> Hgroup:
        return Hgroup(self._tag, self._attributes, self.get_children_from_args(args))

def hgroup(_class: str | None = None, **kwargs: Any) -> Hgroup:
    arguments = { 'class': _class }
    return Hgroup('hgroup', arguments | kwargs, [])

class Header(HTMLElement):

    def __call__(self: Header, *args: Flowcontent | list[Flowcontent]) -> Header:
        return Header(self._tag, self._attributes, self.get_children_from_args(args))

def header(_class: str | None = None, **kwargs: Any) -> Header:
    arguments = { 'class': _class }
    return Header('header', arguments | kwargs, [])

class Footer(HTMLElement):

    def __call__(self: Footer, *args: Flowcontent | list[Flowcontent]) -> Footer:
        return Footer(self._tag, self._attributes, self.get_children_from_args(args))

def footer(_class: str | None = None, **kwargs: Any) -> Footer:
    arguments = { 'class': _class }
    return Footer('footer', arguments | kwargs, [])

class Address(HTMLElement):

    def __call__(self: Address, *args: Flowcontent | list[Flowcontent]) -> Address:
        return Address(self._tag, self._attributes, self.get_children_from_args(args))

def address(_class: str | None = None, **kwargs: Any) -> Address:
    arguments = { 'class': _class }
    return Address('address', arguments | kwargs, [])

class P(HTMLElement):

    def __call__(self: P, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> P:
        return P(self._tag, self._attributes, self.get_children_from_args(args))

def p(_class: str | None = None, **kwargs: Any) -> P:
    arguments = { 'class': _class }
    return P('p', arguments | kwargs, [])

class Br(HTMLElement):
    pass

def br(_class: str | None = None, **kwargs: Any) -> Br:
    arguments = { 'class': _class }
    return Br('br', arguments | kwargs, [])

class Pre(HTMLElement):

    def __call__(self: Pre, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Pre:
        return Pre(self._tag, self._attributes, self.get_children_from_args(args))

def pre(_class: str | None = None, **kwargs: Any) -> Pre:
    arguments = { 'class': _class }
    return Pre('pre', arguments | kwargs, [])

class Dialog(HTMLElement):

    def __call__(self: Dialog, *args: Flowcontent | list[Flowcontent]) -> Dialog:
        return Dialog(self._tag, self._attributes, self.get_children_from_args(args))

def dialog(_class: str | None = None, **kwargs: Any) -> Dialog:
    arguments = { 'class': _class }
    return Dialog('dialog', arguments | kwargs, [])

class Blockquote(HTMLElement):

    def __call__(self: Blockquote, *args: Flowcontent | str | list[Flowcontent | str]) -> Blockquote:
        return Blockquote(self._tag, self._attributes, self.get_children_from_args(args))

def blockquote(_class: str | None = None, **kwargs: Any) -> Blockquote:
    arguments = { 'class': _class }
    return Blockquote('blockquote', arguments | kwargs, [])

class Ol(HTMLElement):

    def __call__(self: Ol, *args: Li | list[Li]) -> Ol:
        return Ol(self._tag, self._attributes, self.get_children_from_args(args))

def ol(_class: str | None = None, **kwargs: Any) -> Ol:
    arguments = { 'class': _class }
    return Ol('ol', arguments | kwargs, [])

class Ul(HTMLElement):

    def __call__(self: Ul, *args: Li | list[Li]) -> Ul:
        return Ul(self._tag, self._attributes, self.get_children_from_args(args))

def ul(_class: str | None = None, **kwargs: Any) -> Ul:
    arguments = { 'class': _class }
    return Ul('ul', arguments | kwargs, [])

class Li(HTMLElement):

    def __call__(self: Li, *args: Flowcontent | str | list[Flowcontent | str]) -> Li:
        return Li(self._tag, self._attributes, self.get_children_from_args(args))

def li(_class: str | None = None, **kwargs: Any) -> Li:
    arguments = { 'class': _class }
    return Li('li', arguments | kwargs, [])

class Dl(HTMLElement):

    def __call__(self: Dl, *args: Dd | Dt | list[Dd | Dt]) -> Dl:
        return Dl(self._tag, self._attributes, self.get_children_from_args(args))

def dl(_class: str | None = None, **kwargs: Any) -> Dl:
    arguments = { 'class': _class }
    return Dl('dl', arguments | kwargs, [])

class Dt(HTMLElement):

    def __call__(self: Dt, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Dt:
        return Dt(self._tag, self._attributes, self.get_children_from_args(args))

def dt(_class: str | None = None, **kwargs: Any) -> Dt:
    arguments = { 'class': _class }
    return Dt('dt', arguments | kwargs, [])

class Dd(HTMLElement):

    def __call__(self: Dd, *args: Flowcontent | str | list[Flowcontent | str]) -> Dd:
        return Dd(self._tag, self._attributes, self.get_children_from_args(args))

def dd(_class: str | None = None, **kwargs: Any) -> Dd:
    arguments = { 'class': _class }
    return Dd('dd', arguments | kwargs, [])

class A(HTMLElement):

    def __call__(self: A, *args: Flowcontent | str | list[Flowcontent | str]) -> A:
        return A(self._tag, self._attributes, self.get_children_from_args(args))

def a(_class: str | None = None, **kwargs: Any) -> A:
    arguments = { 'class': _class }
    return A('a', arguments | kwargs, [])

class Em(HTMLElement):

    def __call__(self: Em, *args: Phrasingcontent | list[Phrasingcontent]) -> Em:
        return Em(self._tag, self._attributes, self.get_children_from_args(args))

def em(_class: str | None = None, **kwargs: Any) -> Em:
    arguments = { 'class': _class }
    return Em('em', arguments | kwargs, [])

class Strong(HTMLElement):

    def __call__(self: Strong, *args: Phrasingcontent | list[Phrasingcontent]) -> Strong:
        return Strong(self._tag, self._attributes, self.get_children_from_args(args))

def strong(_class: str | None = None, **kwargs: Any) -> Strong:
    arguments = { 'class': _class }
    return Strong('strong', arguments | kwargs, [])

class Small(HTMLElement):

    def __call__(self: Small, *args: Phrasingcontent | list[Phrasingcontent]) -> Small:
        return Small(self._tag, self._attributes, self.get_children_from_args(args))

def small(_class: str | None = None, **kwargs: Any) -> Small:
    arguments = { 'class': _class }
    return Small('small', arguments | kwargs, [])

class Cite(HTMLElement):

    def __call__(self: Cite, *args: Phrasingcontent | list[Phrasingcontent]) -> Cite:
        return Cite(self._tag, self._attributes, self.get_children_from_args(args))

def cite(_class: str | None = None, **kwargs: Any) -> Cite:
    arguments = { 'class': _class }
    return Cite('cite', arguments | kwargs, [])

class Q(HTMLElement):

    def __call__(self: Q, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Q:
        return Q(self._tag, self._attributes, self.get_children_from_args(args))

def q(_class: str | None = None, **kwargs: Any) -> Q:
    arguments = { 'class': _class }
    return Q('q', arguments | kwargs, [])

class Dfn(HTMLElement):

    def __call__(self: Dfn, *args: Phrasingcontent | list[Phrasingcontent]) -> Dfn:
        return Dfn(self._tag, self._attributes, self.get_children_from_args(args))

def dfn(_class: str | None = None, **kwargs: Any) -> Dfn:
    arguments = { 'class': _class }
    return Dfn('dfn', arguments | kwargs, [])

class Abbr(HTMLElement):

    def __call__(self: Abbr, *args: Phrasingcontent | list[Phrasingcontent]) -> Abbr:
        return Abbr(self._tag, self._attributes, self.get_children_from_args(args))

def abbr(_class: str | None = None, **kwargs: Any) -> Abbr:
    arguments = { 'class': _class }
    return Abbr('abbr', arguments | kwargs, [])

class Code(HTMLElement):

    def __call__(self: Code, *args: Phrasingcontent | list[Phrasingcontent]) -> Code:
        return Code(self._tag, self._attributes, self.get_children_from_args(args))

def code(_class: str | None = None, **kwargs: Any) -> Code:
    arguments = { 'class': _class }
    return Code('code', arguments | kwargs, [])

class Var(HTMLElement):

    def __call__(self: Var, *args: Phrasingcontent | list[Phrasingcontent]) -> Var:
        return Var(self._tag, self._attributes, self.get_children_from_args(args))

def var(_class: str | None = None, **kwargs: Any) -> Var:
    arguments = { 'class': _class }
    return Var('var', arguments | kwargs, [])

class Samp(HTMLElement):

    def __call__(self: Samp, *args: Phrasingcontent | list[Phrasingcontent]) -> Samp:
        return Samp(self._tag, self._attributes, self.get_children_from_args(args))

def samp(_class: str | None = None, **kwargs: Any) -> Samp:
    arguments = { 'class': _class }
    return Samp('samp', arguments | kwargs, [])

class Kbd(HTMLElement):

    def __call__(self: Kbd, *args: Phrasingcontent | list[Phrasingcontent]) -> Kbd:
        return Kbd(self._tag, self._attributes, self.get_children_from_args(args))

def kbd(_class: str | None = None, **kwargs: Any) -> Kbd:
    arguments = { 'class': _class }
    return Kbd('kbd', arguments | kwargs, [])

class Sub(HTMLElement):

    def __call__(self: Sub, *args: Phrasingcontent | list[Phrasingcontent]) -> Sub:
        return Sub(self._tag, self._attributes, self.get_children_from_args(args))

def sub(_class: str | None = None, **kwargs: Any) -> Sub:
    arguments = { 'class': _class }
    return Sub('sub', arguments | kwargs, [])

class Sup(HTMLElement):

    def __call__(self: Sup, *args: Phrasingcontent | list[Phrasingcontent]) -> Sup:
        return Sup(self._tag, self._attributes, self.get_children_from_args(args))

def sup(_class: str | None = None, **kwargs: Any) -> Sup:
    arguments = { 'class': _class }
    return Sup('sup', arguments | kwargs, [])

class I(HTMLElement):

    def __call__(self: I, *args: Phrasingcontent | list[Phrasingcontent]) -> I:
        return I(self._tag, self._attributes, self.get_children_from_args(args))

def i(_class: str | None = None, **kwargs: Any) -> I:
    arguments = { 'class': _class }
    return I('i', arguments | kwargs, [])

class B(HTMLElement):

    def __call__(self: B, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> B:
        return B(self._tag, self._attributes, self.get_children_from_args(args))

def b(_class: str | None = None, **kwargs: Any) -> B:
    arguments = { 'class': _class }
    return B('b', arguments | kwargs, [])

class Main(HTMLElement):

    def __call__(self: Main, *args: Phrasingcontent | list[Phrasingcontent]) -> Main:
        return Main(self._tag, self._attributes, self.get_children_from_args(args))

def main(_class: str | None = None, **kwargs: Any) -> Main:
    arguments = { 'class': _class }
    return Main('main', arguments | kwargs, [])

class Mark(HTMLElement):

    def __call__(self: Mark, *args: Phrasingcontent | list[Phrasingcontent]) -> Mark:
        return Mark(self._tag, self._attributes, self.get_children_from_args(args))

def mark(_class: str | None = None, **kwargs: Any) -> Mark:
    arguments = { 'class': _class }
    return Mark('mark', arguments | kwargs, [])

class Math(HTMLElement):

    def __call__(self: Math, *args: Phrasingcontent | list[Phrasingcontent]) -> Math:
        return Math(self._tag, self._attributes, self.get_children_from_args(args))

def math(_class: str | None = None, **kwargs: Any) -> Math:
    arguments = { 'class': _class }
    return Math('math', arguments | kwargs, [])

class Progress(HTMLElement):
    pass

def progress(_class: str | None = None, **kwargs: Any) -> Progress:
    arguments = { 'class': _class }
    return Progress('progress', arguments | kwargs, [])

class Meter(HTMLElement):

    def __call__(self: Meter, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Meter:
        return Meter(self._tag, self._attributes, self.get_children_from_args(args))

def meter(_class: str | None = None, **kwargs: Any) -> Meter:
    arguments = { 'class': _class }
    return Meter('meter', arguments | kwargs, [])

class Time(HTMLElement):

    def __call__(self: Time, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Time:
        return Time(self._tag, self._attributes, self.get_children_from_args(args))

def time(_class: str | None = None, **kwargs: Any) -> Time:
    arguments = { 'class': _class }
    return Time('time', arguments | kwargs, [])

class Ruby(HTMLElement):

    def __call__(self: Ruby, *args: Phrasingcontent | Rt | Rp | str | list[Phrasingcontent | Rt | Rp | str]) -> Ruby:
        return Ruby(self._tag, self._attributes, self.get_children_from_args(args))

def ruby(_class: str | None = None, **kwargs: Any) -> Ruby:
    arguments = { 'class': _class }
    return Ruby('ruby', arguments | kwargs, [])

class Rt(HTMLElement):

    def __call__(self: Rt, *args: Phrasingcontent | list[Phrasingcontent]) -> Rt:
        return Rt(self._tag, self._attributes, self.get_children_from_args(args))

def rt(_class: str | None = None, **kwargs: Any) -> Rt:
    arguments = { 'class': _class }
    return Rt('rt', arguments | kwargs, [])

class Rp(HTMLElement):

    def __call__(self: Rp, *args: Phrasingcontent | list[Phrasingcontent]) -> Rp:
        return Rp(self._tag, self._attributes, self.get_children_from_args(args))

def rp(_class: str | None = None, **kwargs: Any) -> Rp:
    arguments = { 'class': _class }
    return Rp('rp', arguments | kwargs, [])

class Bdi(HTMLElement):

    def __call__(self: Bdi, *args: Phrasingcontent | list[Phrasingcontent]) -> Bdi:
        return Bdi(self._tag, self._attributes, self.get_children_from_args(args))

def bdi(_class: str | None = None, **kwargs: Any) -> Bdi:
    arguments = { 'class': _class }
    return Bdi('bdi', arguments | kwargs, [])

class Bdo(HTMLElement):

    def __call__(self: Bdo, *args: Phrasingcontent | list[Phrasingcontent]) -> Bdo:
        return Bdo(self._tag, self._attributes, self.get_children_from_args(args))

def bdo(_class: str | None = None, **kwargs: Any) -> Bdo:
    arguments = { 'class': _class }
    return Bdo('bdo', arguments | kwargs, [])

class Span(HTMLElement):

    def __call__(self: Span, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Span:
        return Span(self._tag, self._attributes, self.get_children_from_args(args))

def span(_class: str | None = None, **kwargs: Any) -> Span:
    arguments = { 'class': _class }
    return Span('span', arguments | kwargs, [])

class Ins(HTMLElement):

    def __call__(self: Ins, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Ins:
        return Ins(self._tag, self._attributes, self.get_children_from_args(args))

def ins(_class: str | None = None, **kwargs: Any) -> Ins:
    arguments = { 'class': _class }
    return Ins('ins', arguments | kwargs, [])

class Figure(HTMLElement):

    def __call__(self: Figure, *args: Flowcontent | Legend | Figcaption | str | list[Flowcontent | Legend | Figcaption | str]) -> Figure:
        return Figure(self._tag, self._attributes, self.get_children_from_args(args))

def figure(_class: str | None = None, **kwargs: Any) -> Figure:
    arguments = { 'class': _class }
    return Figure('figure', arguments | kwargs, [])

class Figcaption(HTMLElement):

    def __call__(self: Figcaption, *args: Flowcontent | str | list[Flowcontent | str]) -> Figcaption:
        return Figcaption(self._tag, self._attributes, self.get_children_from_args(args))

def figcaption(_class: str | None = None, **kwargs: Any) -> Figcaption:
    arguments = { 'class': _class }
    return Figcaption('figcaption', arguments | kwargs, [])

class Img(HTMLElement):
    pass

def img(_class: str | None = None, **kwargs: Any) -> Img:
    arguments = { 'class': _class }
    return Img('img', arguments | kwargs, [])

class Picture(HTMLElement):

    def __call__(self: Picture, *args: Source | Img | list[Source | Img]) -> Picture:
        return Picture(self._tag, self._attributes, self.get_children_from_args(args))

def picture(_class: str | None = None, **kwargs: Any) -> Picture:
    arguments = { 'class': _class }
    return Picture('picture', arguments | kwargs, [])

class Iframe(HTMLElement):
    pass

def iframe(_class: str | None = None, **kwargs: Any) -> Iframe:
    arguments = { 'class': _class }
    return Iframe('iframe', arguments | kwargs, [])

class Embed(HTMLElement):
    pass

def embed(_class: str | None = None, **kwargs: Any) -> Embed:
    arguments = { 'class': _class }
    return Embed('embed', arguments | kwargs, [])

class Object(HTMLElement):

    def __call__(self: Object, *args: Param | str | list[Param | str]) -> Object:
        return Object(self._tag, self._attributes, self.get_children_from_args(args))

def object(_class: str | None = None, **kwargs: Any) -> Object:
    arguments = { 'class': _class }
    return Object('object', arguments | kwargs, [])

class Param(HTMLElement):
    pass

def param(_class: str | None = None, **kwargs: Any) -> Param:
    arguments = { 'class': _class }
    return Param('param', arguments | kwargs, [])

class Details(HTMLElement):

    def __call__(self: Details, *args: Legend | Flowcontent | str | list[Legend | Flowcontent | str]) -> Details:
        return Details(self._tag, self._attributes, self.get_children_from_args(args))

def details(_class: str | None = None, **kwargs: Any) -> Details:
    arguments = { 'class': _class }
    return Details('details', arguments | kwargs, [])

class Command(HTMLElement):
    pass

def command(_class: str | None = None, **kwargs: Any) -> Command:
    arguments = { 'class': _class }
    return Command('command', arguments | kwargs, [])

class Menu(HTMLElement):

    def __call__(self: Menu, *args: Li | Flowcontent | list[Li | Flowcontent]) -> Menu:
        return Menu(self._tag, self._attributes, self.get_children_from_args(args))

def menu(_class: str | None = None, **kwargs: Any) -> Menu:
    arguments = { 'class': _class }
    return Menu('menu', arguments | kwargs, [])

class Legend(HTMLElement):

    def __call__(self: Legend, *args: Flowcontent | Phrasingcontent | str | list[Flowcontent | Phrasingcontent | str]) -> Legend:
        return Legend(self._tag, self._attributes, self.get_children_from_args(args))

def legend(_class: str | None = None, **kwargs: Any) -> Legend:
    arguments = { 'class': _class }
    return Legend('legend', arguments | kwargs, [])

class Div(HTMLElement):

    def __call__(self: Div, *args: Flowcontent | list[Flowcontent]) -> Div:
        return Div(self._tag, self._attributes, self.get_children_from_args(args))

def div(_class: str | None = None, **kwargs: Any) -> Div:
    arguments = { 'class': _class }
    return Div('div', arguments | kwargs, [])

class Source(HTMLElement):
    pass

def source(_class: str | None = None, **kwargs: Any) -> Source:
    arguments = { 'class': _class }
    return Source('source', arguments | kwargs, [])

class Audio(HTMLElement):

    def __call__(self: Audio, *args: Source | str | list[Source | str]) -> Audio:
        return Audio(self._tag, self._attributes, self.get_children_from_args(args))

def audio(_class: str | None = None, **kwargs: Any) -> Audio:
    arguments = { 'class': _class }
    return Audio('audio', arguments | kwargs, [])

class Video(HTMLElement):

    def __call__(self: Video, *args: Source | str | list[Source | str]) -> Video:
        return Video(self._tag, self._attributes, self.get_children_from_args(args))

def video(_class: str | None = None, **kwargs: Any) -> Video:
    arguments = { 'class': _class }
    return Video('video', arguments | kwargs, [])

class Hr(HTMLElement):
    pass

def hr(_class: str | None = None, **kwargs: Any) -> Hr:
    arguments = { 'class': _class }
    return Hr('hr', arguments | kwargs, [])

class Form(HTMLElement):

    def __call__(self: Form, *args: Flowcontent | str | list[Flowcontent | str]) -> Form:
        return Form(self._tag, self._attributes, self.get_children_from_args(args))

def form(_class: str | None = None, **kwargs: Any) -> Form:
    arguments = { 'class': _class }
    return Form('form', arguments | kwargs, [])

class Fieldset(HTMLElement):

    def __call__(self: Fieldset, *args: Legend | Flowcontent | str | list[Legend | Flowcontent | str]) -> Fieldset:
        return Fieldset(self._tag, self._attributes, self.get_children_from_args(args))

def fieldset(_class: str | None = None, **kwargs: Any) -> Fieldset:
    arguments = { 'class': _class }
    return Fieldset('fieldset', arguments | kwargs, [])

class Label(HTMLElement):

    def __call__(self: Label, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Label:
        return Label(self._tag, self._attributes, self.get_children_from_args(args))

def label(_class: str | None = None, **kwargs: Any) -> Label:
    arguments = { 'class': _class }
    return Label('label', arguments | kwargs, [])

class Input(HTMLElement):
    pass

def input(_class: str | None = None, **kwargs: Any) -> Input:
    arguments = { 'class': _class }
    return Input('input', arguments | kwargs, [])

class Button(HTMLElement):

    def __call__(self: Button, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Button:
        return Button(self._tag, self._attributes, self.get_children_from_args(args))

def button(_class: str | None = None, **kwargs: Any) -> Button:
    arguments = { 'class': _class }
    return Button('button', arguments | kwargs, [])

class Select(HTMLElement):

    def __call__(self: Select, *args: Option | Optgroup | list[Option | Optgroup]) -> Select:
        return Select(self._tag, self._attributes, self.get_children_from_args(args))

def select(_class: str | None = None, **kwargs: Any) -> Select:
    arguments = { 'class': _class }
    return Select('select', arguments | kwargs, [])

class Datalist(HTMLElement):

    def __call__(self: Datalist, *args: Option | Phrasingcontent | list[Option | Phrasingcontent]) -> Datalist:
        return Datalist(self._tag, self._attributes, self.get_children_from_args(args))

def datalist(_class: str | None = None, **kwargs: Any) -> Datalist:
    arguments = { 'class': _class }
    return Datalist('datalist', arguments | kwargs, [])

class Optgroup(HTMLElement):

    def __call__(self: Optgroup, *args: Option | list[Option]) -> Optgroup:
        return Optgroup(self._tag, self._attributes, self.get_children_from_args(args))

def optgroup(_class: str | None = None, **kwargs: Any) -> Optgroup:
    arguments = { 'class': _class }
    return Optgroup('optgroup', arguments | kwargs, [])

class Option(HTMLElement):
    pass

def option(_class: str | None = None, **kwargs: Any) -> Option:
    arguments = { 'class': _class }
    return Option('option', arguments | kwargs, [])

class Textarea(HTMLElement):
    pass

def textarea(_class: str | None = None, **kwargs: Any) -> Textarea:
    arguments = { 'class': _class }
    return Textarea('textarea', arguments | kwargs, [])

class Keygen(HTMLElement):
    pass

def keygen(_class: str | None = None, **kwargs: Any) -> Keygen:
    arguments = { 'class': _class }
    return Keygen('keygen', arguments | kwargs, [])

class Output(HTMLElement):

    def __call__(self: Output, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Output:
        return Output(self._tag, self._attributes, self.get_children_from_args(args))

def output(_class: str | None = None, **kwargs: Any) -> Output:
    arguments = { 'class': _class }
    return Output('output', arguments | kwargs, [])

class Canvas(HTMLElement):
    pass

def canvas(_class: str | None = None, **kwargs: Any) -> Canvas:
    arguments = { 'class': _class }
    return Canvas('canvas', arguments | kwargs, [])

class Map(HTMLElement):

    def __call__(self: Map, *args: Phrasingcontent | Flowcontent | list[Phrasingcontent | Flowcontent]) -> Map:
        return Map(self._tag, self._attributes, self.get_children_from_args(args))

def map(_class: str | None = None, **kwargs: Any) -> Map:
    arguments = { 'class': _class }
    return Map('map', arguments | kwargs, [])

class Area(HTMLElement):
    pass

def area(_class: str | None = None, **kwargs: Any) -> Area:
    arguments = { 'class': _class }
    return Area('area', arguments | kwargs, [])

class Mathml(HTMLElement):
    pass

def mathml(_class: str | None = None, **kwargs: Any) -> Mathml:
    arguments = { 'class': _class }
    return Mathml('mathml', arguments | kwargs, [])

class Svg(HTMLElement):
    pass

def svg(_class: str | None = None, **kwargs: Any) -> Svg:
    arguments = { 'class': _class }
    return Svg('svg', arguments | kwargs, [])

class Table(HTMLElement):

    def __call__(self: Table, *args: Caption | Colgroup | Thead | Tfoot | Tbody | Tr | list[Caption | Colgroup | Thead | Tfoot | Tbody | Tr]) -> Table:
        return Table(self._tag, self._attributes, self.get_children_from_args(args))

def table(_class: str | None = None, **kwargs: Any) -> Table:
    arguments = { 'class': _class }
    return Table('table', arguments | kwargs, [])

class Caption(HTMLElement):

    def __call__(self: Caption, *args: Flowcontent | list[Flowcontent]) -> Caption:
        return Caption(self._tag, self._attributes, self.get_children_from_args(args))

def caption(_class: str | None = None, **kwargs: Any) -> Caption:
    arguments = { 'class': _class }
    return Caption('caption', arguments | kwargs, [])

class Colgroup(HTMLElement):

    def __call__(self: Colgroup, *args: Col | list[Col]) -> Colgroup:
        return Colgroup(self._tag, self._attributes, self.get_children_from_args(args))

def colgroup(_class: str | None = None, **kwargs: Any) -> Colgroup:
    arguments = { 'class': _class }
    return Colgroup('colgroup', arguments | kwargs, [])

class Col(HTMLElement):
    pass

def col(_class: str | None = None, **kwargs: Any) -> Col:
    arguments = { 'class': _class }
    return Col('col', arguments | kwargs, [])

class Thead(HTMLElement):

    def __call__(self: Thead, *args: Tr | list[Tr]) -> Thead:
        return Thead(self._tag, self._attributes, self.get_children_from_args(args))

def thead(_class: str | None = None, **kwargs: Any) -> Thead:
    arguments = { 'class': _class }
    return Thead('thead', arguments | kwargs, [])

class Tfoot(HTMLElement):

    def __call__(self: Tfoot, *args: Tr | list[Tr]) -> Tfoot:
        return Tfoot(self._tag, self._attributes, self.get_children_from_args(args))

def tfoot(_class: str | None = None, **kwargs: Any) -> Tfoot:
    arguments = { 'class': _class }
    return Tfoot('tfoot', arguments | kwargs, [])

class Tbody(HTMLElement):

    def __call__(self: Tbody, *args: Tr | list[Tr]) -> Tbody:
        return Tbody(self._tag, self._attributes, self.get_children_from_args(args))

def tbody(_class: str | None = None, **kwargs: Any) -> Tbody:
    arguments = { 'class': _class }
    return Tbody('tbody', arguments | kwargs, [])

class Tr(HTMLElement):

    def __call__(self: Tr, *args: Th | Td | list[Th | Td]) -> Tr:
        return Tr(self._tag, self._attributes, self.get_children_from_args(args))

def tr(_class: str | None = None, **kwargs: Any) -> Tr:
    arguments = { 'class': _class }
    return Tr('tr', arguments | kwargs, [])

class Th(HTMLElement):

    def __call__(self: Th, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Th:
        return Th(self._tag, self._attributes, self.get_children_from_args(args))

def th(_class: str | None = None, **kwargs: Any) -> Th:
    arguments = { 'class': _class }
    return Th('th', arguments | kwargs, [])

class Td(HTMLElement):

    def __call__(self: Td, *args: Flowcontent | str | list[Flowcontent | str]) -> Td:
        return Td(self._tag, self._attributes, self.get_children_from_args(args))

def td(_class: str | None = None, **kwargs: Any) -> Td:
    arguments = { 'class': _class }
    return Td('td', arguments | kwargs, [])

Metadatacontent = Base | Command | Link | Meta | Noscript | Script | Style | Title
Flowcontent = A | Abbr | Area | Address | Article | Aside | Audio | B | Bdi | Blockquote | Bdo | Br | Button | Canvas | Cite | Code | Command | Datalist | Details | Dfn | Dialog | Div | Dl | Em | Embed | Fieldset | Figure | Figcaption | Footer | Form | H1 | H2 | H3 | H4 | H5 | H6 | Header | Hgroup | Hr | I | Iframe | Img | Picture | Input | Ins | Kbd | Keygen | Label | Link | Main | Map | Mark | Math | Menu | Meta | Meter | Nav | Noscript | Ol | Object | Output | P | Pre | Progress | Q | Ruby | Samp | Script | Section | Select | Small | Span | Strong | Style | Summary | Sub | Sup | Svg | Table | Textarea | Time | Ul | Var | Video
Headingcontent = H1 | H2 | H3 | H4 | H5 | H6 | Hgroup
Sectioningcontent = Article | Aside | Main | Nav | Section
Phrasingcontent = A | Abbr | Area | Audio | B | Bdi | Bdo | Br | Button | Canvas | Cite | Code | Command | Datalist | Dfn | Em | Embed | I | Iframe | Img | Picture | Input | Ins | Kbd | Keygen | Label | Link | Map | Mark | Math | Meta | Meter | Noscript | Object | Output | Progress | Q | Ruby | Samp | Script | Select | Small | Span | Strong | Sub | Sup | Svg | Textarea | Time | Var | Video
Interactivecontent = A | Audio | Button | Details | Embed | Iframe | Img | Picture | Input | Keygen | Label | Menu | Object | Select | Textarea | Video
