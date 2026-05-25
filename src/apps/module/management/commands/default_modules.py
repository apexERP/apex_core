from django.core.management.base import BaseCommand

from apps.module.models import Module, ModulePrice


class Command(BaseCommand):

    help = 'Seed default ERP modules'

    def handle(self, *args, **kwargs):

        modules = self.get_modules()
        for item in modules:

            module, created = Module.objects.get_or_create(
                name=item['name'],
                defaults={
                    'title': item['title'],
                    'description': item['description'],
                    'order': item['order']
                }
            )

            ModulePrice.objects.update_or_create(
                module=module,
                defaults={
                    'standart_price': item['plans']['standard']['price'],
                    'standart_features': '\n'.join(
                        item['plans']['standard']['features']
                    ),

                    'pro_price': item['plans']['pro']['price'],
                    'pro_features': '\n'.join(
                        item['plans']['pro']['features']
                    ),

                    'premium_price': item['plans']['premium']['price'],
                    'premium_features': '\n'.join(
                        item['plans']['premium']['features']
                    ),
                }
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Created module: {module.name}'
                    )
                )

            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Updated module: {module.name}'
                    )
                )

        self.stdout.write(
            self.style.SUCCESS('Modules seeded successfully.')
        )
        
        
    def get_modules(self):
        modules = [
            {
                'name': 'pos',
                'title': 'Point of Sale',
                'description': 'Point of Sale system',
                'order': 1,
                'plans': {
                    'standard': {
                        'price': 100,
                        'features': [
                            'Basic POS',
                            '1 Branch',
                            'Basic Reports'
                        ]
                    },
                    'pro': {
                        'price': 200,
                        'features': [
                            'Advanced POS',
                            '5 Branches',
                            'Inventory Integration',
                            'Analytics'
                        ]
                    },
                    'premium': {
                        'price': 300,
                        'features': [
                            'Unlimited Branches',
                            'AI Analytics',
                            'Priority Support',
                            'API Access'
                        ]
                    }
                }
            },

            {
                'name': 'e_commerce',
                'title': 'E-Commerce',
                'description': 'Online commerce platform',
                'order': 2,
                'plans': {
                    'standard': {
                        'price': 150,
                        'features': [
                            'Online Store',
                            'Product Catalog',
                            'Basic Checkout'
                        ]
                    },
                    'pro': {
                        'price': 300,
                        'features': [
                            'Multi Vendor',
                            'Advanced Payments',
                            'Discount System',
                            'Analytics'
                        ]
                    },
                    'premium': {
                        'price': 500,
                        'features': [
                            'AI Recommendations',
                            'Marketplace Features',
                            'Custom API',
                            'Enterprise Scaling'
                        ]
                    }
                }
            },

            {
                'name': 'b2b_market',
                'title': 'B2B Marketplace',
                'description': 'Business-to-business marketplace',
                'order': 3,
                'plans': {
                    'standard': {
                        'price': 200,
                        'features': [
                            'Supplier Management',
                            'Company Profiles',
                            'Basic Orders'
                        ]
                    },
                    'pro': {
                        'price': 400,
                        'features': [
                            'Bulk Orders',
                            'RFQ System',
                            'Contract Management'
                        ]
                    },
                    'premium': {
                        'price': 700,
                        'features': [
                            'Enterprise Procurement',
                            'AI Matching',
                            'Advanced Analytics'
                        ]
                    }
                }
            },

            {
                'name': 'inventory',
                'title': 'Inventory Management',
                'description': 'Inventory and warehouse management',
                'order': 4,
                'plans': {
                    'standard': {
                        'price': 120,
                        'features': [
                            'Stock Tracking',
                            'Single Warehouse',
                            'Basic Reports'
                        ]
                    },
                    'pro': {
                        'price': 250,
                        'features': [
                            'Multi Warehouse',
                            'Barcode Support',
                            'Stock Transfers'
                        ]
                    },
                    'premium': {
                        'price': 450,
                        'features': [
                            'AI Forecasting',
                            'Automation',
                            'Advanced Warehousing'
                        ]
                    }
                }
            },

            {
                'name': 'accounting',
                'title': 'Accounting',
                'description': 'Financial accounting system',
                'order': 5,
                'plans': {
                    'standard': {
                        'price': 180,
                        'features': [
                            'Invoices',
                            'Expenses',
                            'Basic Accounting'
                        ]
                    },
                    'pro': {
                        'price': 350,
                        'features': [
                            'Payroll',
                            'Tax Management',
                            'Financial Reports'
                        ]
                    },
                    'premium': {
                        'price': 600,
                        'features': [
                            'Multi Company',
                            'AI Analytics',
                            'Audit Tools'
                        ]
                    }
                }
            },

            {
                'name': 'manufacturing',
                'title': 'Manufacturing',
                'description': 'Production management system',
                'order': 6,
                'plans': {
                    'standard': {
                        'price': 250,
                        'features': [
                            'Production Orders',
                            'BOM',
                            'Basic Scheduling'
                        ]
                    },
                    'pro': {
                        'price': 500,
                        'features': [
                            'MRP',
                            'Quality Control',
                            'Machine Tracking'
                        ]
                    },
                    'premium': {
                        'price': 900,
                        'features': [
                            'AI Optimization',
                            'IoT Integration',
                            'Advanced Planning'
                        ]
                    }
                }
            },

            {
                'name': 'hr',
                'title': 'Human Resources',
                'description': 'HR and employee management',
                'order': 7,
                'plans': {
                    'standard': {
                        'price': 100,
                        'features': [
                            'Employee Records',
                            'Attendance',
                            'Basic HR'
                        ]
                    },
                    'pro': {
                        'price': 220,
                        'features': [
                            'Payroll',
                            'Recruitment',
                            'Performance Tracking'
                        ]
                    },
                    'premium': {
                        'price': 400,
                        'features': [
                            'AI Recruitment',
                            'Advanced Analytics',
                            'Employee Self Service'
                        ]
                    }
                }
            },

            {
                'name': 'logistics',
                'title': 'Logistics',
                'description': 'Transport and logistics management',
                'order': 8,
                'plans': {
                    'standard': {
                        'price': 170,
                        'features': [
                            'Shipment Tracking',
                            'Basic Fleet',
                            'Delivery Reports'
                        ]
                    },
                    'pro': {
                        'price': 350,
                        'features': [
                            'Fleet Management',
                            'GPS Tracking',
                            'Route Optimization'
                        ]
                    },
                    'premium': {
                        'price': 650,
                        'features': [
                            'AI Logistics',
                            'Real-Time Monitoring',
                            'Enterprise Scaling'
                        ]
                    }
                }
            },

            {
                'name': 'apex_pay',
                'title': 'Apex Pay',
                'description': 'Payment processing system',
                'order': 9,
                'plans': {
                    'standard': {
                        'price': 80,
                        'features': [
                            'Payment Gateway',
                            'Transactions',
                            'Basic Security'
                        ]
                    },
                    'pro': {
                        'price': 180,
                        'features': [
                            'Subscriptions',
                            'Fraud Detection',
                            'Advanced Reports'
                        ]
                    },
                    'premium': {
                        'price': 350,
                        'features': [
                            'AI Fraud Protection',
                            'Multi Currency',
                            'Enterprise APIs'
                        ]
                    }
                }
            },

            {
                'name': 'apex_ai',
                'title': 'Apex AI',
                'description': 'AI automation and analytics',
                'order': 10,
                'plans': {
                    'standard': {
                        'price': 300,
                        'features': [
                            'Basic AI Assistant',
                            'Automation',
                            'Predictions'
                        ]
                    },
                    'pro': {
                        'price': 600,
                        'features': [
                            'Advanced AI',
                            'Workflow Automation',
                            'Custom Models'
                        ]
                    },
                    'premium': {
                        'price': 1200,
                        'features': [
                            'Enterprise AI',
                            'Private AI Models',
                            'Full AI Platform'
                        ]
                    }
                }
            },

            {
                'name': 'apex_bi',
                'title': 'Apex BI',
                'description': 'Business intelligence platform',
                'order': 11,
                'plans': {
                    'standard': {
                        'price': 150,
                        'features': [
                            'Dashboards',
                            'Reports',
                            'Basic Charts'
                        ]
                    },
                    'pro': {
                        'price': 320,
                        'features': [
                            'Advanced Analytics',
                            'Real-Time Data',
                            'Custom Dashboards'
                        ]
                    },
                    'premium': {
                        'price': 700,
                        'features': [
                            'AI Insights',
                            'Big Data Analytics',
                            'Enterprise BI'
                        ]
                    }
                }
            }
        ]
        
        
        return modules